import ftputil

dl_dir = "C:/Weather Generator/Rglimclim_1.3-4/TestData/"
# Download some files from the login directory.
with ftputil.FTPHost("ftpcimis.water.ca.gov", "anonymous", "anonymous") as ftp_host:
    ftp_host.chdir("/pub2/annual")
    names = ftp_host.listdir(ftp_host.curdir)
    for name in names:
        if ftp_host.path.isfile(name):
            ftp_host.download(name, dl_dir + name)  # remote, local
            print("Downloaded {0}".format(name))

