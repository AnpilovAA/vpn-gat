# ==================== CONFIGURATION ====================
QUERY_FILE = "queries.txt"                               ## Better compact with:
                                                         ##   ./minify-dict.sh full_dict_file > ./queries.txt
                                                         ## but full ones also work
                                                         
URL_TEMPLATE = "https://www.google.fr/search?q={}"       ## Use national google domain here if exists
DELAY_SECONDS = 40                                       ## Terminate the browser after XX sec
EXPECTED_WAN_IP = "YourExtIPHere"                        ## Populate yourself for your proxy
PROFILES_DIR = "/home/user/vpngat"
PROF_PER_SCREEN = 3
#LAT_MIN, LAT_MAX = 52.29, 52.42        ## Amsterdam NL
#LON_MIN, LON_MAX = 4.80, 4.99          ## Amsterdam NL
LAT_MIN, LAT_MAX = 48.78, 48.95        ## Paris FR
LON_MIN, LON_MAX = 2.21, 2.59          ## Paris FR
#LAT_MIN, LAT_MAX = 59.30, 59.34         ## Stockholm SE
#LON_MIN, LON_MAX = 18.02, 18.10         ## Stockholm SE

RESOLUTIONS = [
    (1280, 720),   # 16:9 HD
    (1366, 768),   # 16:9
    (1600, 900),   # 16:9
    (1920, 1080),  # 16:9 Full HD
    (1280, 960),   # 4:3
    (1400, 1050),  # 4:3
    (1024, 768),   # 4:3
    (1280, 1024)   # 4:3
]

# Change to "chromium-browser" if needed on your system
CHROMIUM_CMD = "chromium"