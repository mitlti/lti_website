import csv
from collections import namedtuple


def read_bios():
    mapping = {
        "Athena": "athena",
        "Timestamp": "timestamp",
        "First Name": "first",
        "Last Name": "last",
        "Executive Position": "position",
        "Course": "course",
        "Year": "year",
        "Activities": "activities",
        "Short (Max. 200 word) biography about yourself.": "bio",
        "WIll you email Phu a picture of yourself?": "phu",
        "Interests": "interests",
        "Hometown": "hometown",
        "Why did you join LTI?": "why"
    }

    bio_fields = ['athena', 'first', 'last', 'position', 'bio']
    Bio = namedtuple('Bio', bio_fields)

    bios = []
    with open('lti-bios.csv') as bios_csv:
        bios_reader = csv.DictReader(bios_csv)
        for bio_row in bios_reader:
            fields = {}
            for k, v in bio_row.iteritems():
                if k is not None and mapping[k] in bio_fields:
                    fields[mapping[k]] = v
            bio = Bio(**fields)
            bios.append(bio)
        return bios

if __name__ == '__main__':
    #bios = read_bios()
    #for bio in bios:
    #    print "%s %s" % (bio.athena, bio.bio)
    with open('test.txt') as test:
        for row in test:
            print unicode(row)
