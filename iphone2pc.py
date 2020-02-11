from icloudpd.authentication import authenticate, TwoStepAuthRequiredError
from icloudpd import download
from icloudpd.email_notifications import send_2sa_notification
from icloudpd.string_helpers import truncate_middle
from icloudpd.autodelete import autodelete_photos
from icloudpd.paths import local_download_path
from icloudpd import exif_datetime
# Must import the constants object so that we can mock values in tests.
from icloudpd import constants
import datetime



try:
    icloud = authenticate(
        'astremskaya@mail.ru',
        'Julia120786'
    )

except TwoStepAuthRequiredError:
    print('ERROR!')
    exit(1)

# Default album is "All Photos", so this is the same as
# calling `icloud.photos.all`.
albums = icloud.photos.albums
print(albums)

photos = icloud.photos.albums['All Photos']
print(len(photos))

for photo in photos:
    if photo.created.strftime('%Y%m') in ('201803','201804','201805','201806'):
        photo_created = photo.created.strftime('%Y%m%d')
        photo_added = photo.added_date.strftime('%Y%m%d')
        print(photo, photo.filename, photo.item_type, photo_created, photo_added)
        download = photo.download()
        with open('d:\\iPhone_photos_2018\\' + photo_created + '_' + photo.filename, 'wb') as opened_file:
            opened_file.write(download.raw.read())

print('~~~ DONE ~~~')
