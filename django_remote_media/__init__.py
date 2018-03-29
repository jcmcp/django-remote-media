import os
import tempfile
import requests
from django.core.files import File

try:
    from urllib.parse import urlparse
except ImportError:
    import urlparse


def django_remote_media(remote_media_url):

    request = requests.get(remote_media_url, stream=True)

    if request.status_code == requests.codes.ok:

        remote_media_basename = os.path.basename(urlparse(remote_media_url).path)

        remote_media_tempfile = tempfile.NamedTemporaryFile()

        for block in request.iter_content(1024 * 8):

            if not block:
                break

            remote_media_tempfile.write(block)

        return remote_media_basename, File(remote_media_tempfile)
