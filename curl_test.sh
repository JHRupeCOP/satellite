SATELLITE_URL="https://satellite.conocophillips.net"
USERNAME="ruppej"
PASSWORD=""

# curl -X GET -s -k -u "$USERNAME:$PASSWORD" "${SATELLITE_URL}/katello/api/host_collections" | python3 -m json.tool
# curl -X GET -s -k -u "$USERNAME:$PASSWORD" "${SATELLITE_URL}/api/hosts" | python3 -m json.tool
# curl -X GET -s -k -u "$USERNAME:$PASSWORD" "${SATELLITE_URL}/katello/api/environments" | python3 -m json.tool
curl -X GET -s -k -u "$USERNAME:$PASSWORD" "${SATELLITE_URL}/katello/api/content_views/4/content_view_versions" | python3 -m json.tool

