SATELLITE_URL="https://satellite.conocophillips.net"
USERNAME="ruppej"
PASSWORD=

curl -X GET -s -k -u "$USERNAME:$PASSWORD" "${SATELLITE_URL}/katello/api/host_collections" | python3 -m json.tool

