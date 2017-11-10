import urllib2
import os

URL = 'ftp://ftp.nersc.no/pub/nansat/test_data/meris_l1/'
SAVE_PATH = 'data'


def download_files(url, save_path):
    """Download data from the ftp server and save them to the """
    request = urllib2.urlopen(url)
    content = request.read()
    files = [el.strip().split()[-1] for el in content.split('\n')[:-1]]
    for f in files:
        if f in os.listdir(save_path):
            print 'The file %s already exist in the %s directory' % (f, save_path)
        else:
            print 'Download: %s' % f
            with open(os.path.join(save_path, f), 'wb') as data_file:
                data_file.write(urllib2.urlopen(os.path.join(url, f)).read())
                data_file.close()


if __name__ == "__main__":
    try:
        os.mkdir('data')
    except OSError:
        pass

    download_files(URL, SAVE_PATH)
    os.system('python ~/geospaas_project/manage.py ingest /vagrant/shared/django-fun/data/*')
    print 'Data were added to the geo-spaas'
