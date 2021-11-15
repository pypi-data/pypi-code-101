import zippyshare


link = "https://www10.zippyshare.com/v/x2m7R4Eh/file.html"

# get direct download link for download managers
print(
    link,
    zippyshare.ZS.get_link(link),
)

# refresh 30 days expiry / time to die
# in order to check new TTD of the file, you need to wait 6-12 hours for zippyshare to refresh the TTD
# the principle is to fetch a few bytes of the remote file with original request session
print(zippyshare.ZS.refresh_ttd(link).headers)
