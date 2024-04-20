# fatmap_json_to_jpx.py
# convert a fatmap json request into a gpx file using the gps data
import sys
import json


def write_gpx(points, output_filename, name, description):
    with open(output_filename, "w") as file:
        # Write the GPX file header and a track segment open tag
        file.write(
            '<?xml version="1.0" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" creator="GaiaGPS" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"><trk><name>{}</name><desc>{}</desc><extensions><line xmlns="http://www.topografix.com/GPX/gpx_style/0/2"><color>00A478</color></line></extensions><trkseg>\n'.format(
                name, description
            )
        )

        # Iterate through the points and write each as a GPX track point
        for lon, lat, elevation in points:
            file.write('  <trkpt lat="{}" lon="{}">\n'.format(lat, lon))
            file.write("    <ele>{}</ele>\n".format(elevation))
            file.write("  </trkpt>\n")

        # Close the GPX tag
        file.write("</trkseg></trk></gpx>\n")


json_file = sys.argv[1]

json_obj = json.load(open(json_file))

name = json_obj["data"]["adventures"][0]["name"]

description = json_obj["data"]["adventures"][0]["description"]

points = json_obj["data"]["adventures"][0]["geo_json"]["coordinates"][0]

write_gpx(points, json_file.replace(".json", ".gpx"), name, description)
