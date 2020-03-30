import xml.etree.ElementTree as ET
import os

# Basic implementation of various parts of the OVE
# project format.

# https://github.com/olive-editor/olive/wiki/About-The-Project-File

# Not complete, just enough to get the tasks I needed done.
# Do not use this on untrusted input.


# Basically, use this class to update an existing Footage object.
class OliveFootage:
    def __init__(
        self,
        props
    ):
        self.props = props


class OliveProject:
    def __init__(self):
        pass

    def open(self, filename):
        self.project = ET.parse(filename)
        self.root = ET.parse(filename).getroot()

    def write(self, filename, project_dir):
        # update the url
        baseDir = os.getcwd()
        path = '{}/{}/{}'.format(
            baseDir,
            project_dir,
            filename
        )
        self.root.find('url').text = path

        ET.ElementTree(self.root).write(path)

    def path(self):
        return self.root.find('url').text

    # Dump a list of media.
    def media(self):
        footages = []
        media = self.root.find('media').findall('footage')
        for footage in media:
            temp = OliveFootage(footage.attrib)
            footages.append(temp)

        return footages

    @staticmethod
    def _update_attrib(base, key, value):
        base.set(key, value)

    def update_media(self, new_footage):
        # find the footage by id
        base = self.root.find('media').findall(
            './/*[@id=\'{}\']/'.format(new_footage.props['id'])
        )[0]

        # Modify if we can
        if base is None:
            return False
        for key, value in new_footage.props.items():
            OliveProject._update_attrib(base, key, value)

        return True


if __name__ == '__main__':
    op = OliveProject()
    op.open('./templates/olive_template.ove')
    print(op.path())
    for item in op.media():
        print(item.props['name'], item.props['url'])
        item.props['name'] = 'test'
        op.update_media(item)
    for item in op.media():
        print(item.props['name'], item.props['url'])


