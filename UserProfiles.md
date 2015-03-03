### Axel ###

Axel is a researcher at McMurdo Station -- a research station based in
the Antarctic. Unfortunately, due to environmental conditions, Axel's
data is actually stored on a file server located in Berkeley,
California.

Normally, Axel's data connection is very solid and rarely goes down,
but unfortunately when working on a file located more than 12500 miles
away, the latency between his local computer and the fileserver is
more than a second in both directions. When working on a spreadsheet
containing time-lapse results of a year-long observation of the ice
there, he saves quite often. Ideally, Axel would like his saves to
local disk to be immediate, with only the small incremental changes to
the file uploaded over a period of time.

### Hans ###

Hans is the lead physical therapist for his company, Scandanavian Neck
and Back Care. During his day-to-day duties of seeing patients and
helping them get back into the swing of things, he keeps track of how
each of them are doing in many disorganized files in his home
directory.

Recently during a morning consultation with a patient recovering from
a crushed disc caused by a flying hippo, Hans' file server randomly
failed to accept writes to his notes. Later on, at about noon, the
file server eventually crashed completely, leaving him without his
notes entirely. Ideally, Hans would like all of his writes to be
stored locally first and propagated later, with often-read data
already cached locally as well.

### Helga ###

Helga is a systems administrator for the Yggdrasil web hosting
company. Being a company that symbolizes the tree of life and the home
of the Norse Gods, they occasionally get requests to host most of the
lesser God's blogs and websites. Unfortunately, being a web hosting
company for the Gods, downtime is unacceptible. In fact, the last
major outage they had resulted in the last systems adminsitrator being
fried on the spot when Thor couldn't post his latest blog entry about
olive pizza.

Helga's systems mostly serve static content, but she hates having to
manually use rsync to update it on her web farm. She's tried using NFS
to solve this problem, but when her fileserver dies off, the entire
system fails. Ideally, she would prefer a combination of NFS and
rsync, so when the fileserver falls apart the web frontends can
continue serving content with no downtime.

### Yojimbo ###

A respectful and technologically advanced ronin, Yojimbo is often seen
wandering from place to place protecting others and their property for
a price. Unfortunately, with all of this travelling, he has little
time to fight with syncronization between his laptop and server at
home.

Recently, Yojimbo accepted a client in Washington state and has less
than an hour to catch the flight to meet them. While working on the
invoice for his last client's services, he lost track of time and
quickly suspended his laptop (without unmounting his NFS home
directory or closing the spreadsheet) while running out of his
apartment. While sitting on the plane, he would like to pick up where
he left off and continue working the invoice to completion.