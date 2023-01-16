from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class CustomStaticFilesStorage(ManifestStaticFilesStorage):

    def file_hash(self, name, content=None):
        hash = super().file_hash(name, content)
        return "PREFIXED_HASH_%s" % hash
