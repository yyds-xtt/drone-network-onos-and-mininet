# MAIN
ASSIGNMENT_METHOD = "ADAPTIVE"  # AGGRESSIVE, ADAPTIVE or OPTIMUM
WAIT_PREVIOUS_TASK_TO_BE_PROCESSED = False
TASK_GENERATION_INTERVAL = 8
SUMO_SEED_TO_USE = 1
DRONE_ID_CLOSE_TO_BS = SUMO_SEED_TO_USE
CASE = "vehicle_speed_v6/20"
SUMO_CFG_PATH = "/home/onur/Coding/projects/sdnCaching/configs/besiktas-2/osm.sumocfg"

USE_RECORD = False
RECORD_FILE = "records/request_interval/lambda15_seed1"

TASK_FAILURE_PENALTY_OFFSET = 60
SIMULATION_DURATION = 1000
TASK_GENERATION_START_TIME = 150
TASK_GENERATION_END_TIME = 750
TASK_SIZE = (30000, 40000)
DEADLINE = (50, 120)
LOG_LEVEL = "ERROR"
# LOG_LEVEL = "DEBUG"
MN_WIFI_LOG_LEVEL = "ERROR"
NUMBER_OF_DRONES = 9
NUMBER_OF_STATIONS = 45
IS_REMOTE_CONTROLLER = True
GENERATOR_ACTIVE_TASKS_MAX = 3
ALLOWED_MAX_TX_TIME = 250

# RANDOMNESS CONTROL
USE_RANDOM_SUMO_SEED = False
SELECT_RANDOM_DRONE_FOR_BS_CONNECTION = False
BS_LOCATION_PRESET = [50, 50]

# MOVEMENT
RANDOM_DRONE_MOVEMENT = False
FIGURE_8_DRONE_MOVEMENT = True
FIGURE_8_ALPHA_VAR = 10
FIGURE_8_PERIOD = 20
COORDINATE_LIMIT_X = (0, 1500)
COORDINATE_LIMIT_Y = (-50, 1250)
UNASSOCIATED_CAR_LOCATION = "-9999,-9999,1"
AVERAGE_HEIGHT = 100
BS_HEIGHT = 10
HEIGHT_DEVIATION = 3

# SUMO TRACI
SKIPPED_STEPS = 130
SUMO_BINARY = "sumo-gui"
# SUMO_CFG_PATH = "/home/onur/Coding/projects/sdnCaching/configs/besiktas-2-satellite/osm.sumocfg"
# SUMO_SIMULATED_DATA_PATH = "/home/onur/Coding/projects/sdnCaching/configs/besiktas-speed-40/sumo_results.xml"
VEHICLE_PREFIX = "veh"
START_SIMULATION_DIRECTLY = True
SUMO_DELAY = 1  # in ms
SIMULATION_STEP_DELAY = 1000  # in ms
VEHICLE_CATEGORY_DISTRIBUTION = ['E'] * 6 + ['T'] * 12 + ['A'] * 5 + ['B'] * 10 #+ ['P'] * 20
DEFAULT_VEHICLE_CLASS = "passenger"
HIGHLIGHT_CARS = False
HIGHLIGHT_AP_RANGE = True
PROCESSOR_VEHICLE_TYPES = ["A", "B"]
TASK_GENERATOR_VEHICLE_TYPES = ["E", "T"]
VEHICLE_TYPE_PROPERTIES = {
    # Task generators
    "E": {"type": "emergency", "shape": "emergency", "color": "red",
          "priority": 0.7, "type_abbreviation": "E"},
    "T": {"type": "emergency", "shape": "firebrigade", "color": "red",
          "priority": 0.3, "type_abbreviation": "T"},
    # Processors
    "A": {"type": "trailer", "shape": "truck/semitrailer", "color": "purple",
          "process_speed": 2000, "queue_size": 100000, "type_abbreviation": "A"},
          # "process_speed": 5000, "queue_size": 100000, "type_abbreviation": "A"},
          # "process_speed": 700, "queue_size": 100000, "type_abbreviation": "A"},
    "B": {"type": "bus", "shape": "bus", "color": "cyan",
          "process_speed": 1500, "queue_size": 70000, "type_abbreviation": "B"},
          # "process_speed": 4000, "queue_size": 70000, "type_abbreviation": "B"},
          # "process_speed": 500, "queue_size": 70000, "type_abbreviation": "B"},

    # Other
    "V": {"type": "vip", "shape": "vip", "color": "magenta", "type_abbreviation": "V"},
    "P": {"type": "private", "shape": "passenger/sedan", "color": "pink", "type_abbreviation": "P"},
}
# WIFI
AP_AP_RSSI = -50
WIFI_NOISE_THRESHOLD = -80
REAL_LIFE_RANGE_COEFFICIENT = 0.85
AP_AP_RANGE = 450 * REAL_LIFE_RANGE_COEFFICIENT
AP_GROUND_RANGE = 330 * REAL_LIFE_RANGE_COEFFICIENT  # 368 * cos(15.9) = 351
AP_DIRECT_RANGE = 368 * REAL_LIFE_RANGE_COEFFICIENT  # Used for simulation data generation
# POWER
ANTENNA_GAIN = 3
DRONE_AP_TX_POWER = 23
DRONE_MESH_TX_POWER = 23
BS_MESH_TX_POWER = 23
VEHICLE_TX_POWER = 23

# CONTROLLER
MININET_IP = "127.0.0.1"
UPDATE_SW_LOCATIONS_ON_ONOS = False
USE_LAT_LON = False
CONTROLLER_AP_ID = 4

# TRAFFIC
GENERATE_TRAFFIC = True
USE_IPERF = True
DITG_CONTROL_PORTS = []

# CLOUD
NAT_HOST_ID = 211
CLOUD_PROCESSOR_SPEED = 3000
CLOUD_PROBABILITY_BY_POOL_SIZE = {
    0: 0,
    3: 0.3,
    7: 0.7,
    10: 0.9
}
CLOUD_LINK_DELAY = "18ms"

# COMMUNICATION
TASK_ASSIGNER_SERVER = "CONTROLLER_HOST"  # BS_HOST, NAT, CONTROLLER_HOST
CLOUD_SERVER = "BS_HOST"  # BS_HOST, NAT
TASK_REQUEST_LISTEN_PORT = 8701
IPERF_PORT_RANGE_START = 9000

# OTHER
START_XTERM = False
NUMBER_OF_DRONES_PER_ROW = 3
NUMBER_OF_DRONES_PER_COLUMN = 3
CONTROLLER_IP = "127.0.0.1"
AP_NAME_PREFIX = "ap"
BS_NAME_PREFIX = "bs"
BS_ID_OFFSET = 100
BS_GROUND_RANGE = 100
BS_GROUND_ANTENNA_GAIN = -5
BS_GROUND_TX_POWER = 1
ADD_DRONE_MN_HOST = False
PLOT_MININET_GRAPH = False

# DITG
ITG_SENDER_LOG_PATH = "ditgSenderLogs"
ITG_RECEIVER_LOG_PATH = "ditgReceiverLogs"
ITG_LOG_SERVER_IP = None

# CONFIGS BELOW ARE NOT USED
# ENERGY
INITIAL_DRONE_BATTERY_CAPACITY = 187545.6  # Joule(Ws) 0.8 * 65.12Wh=4.4Ah@14.8V %20 Reserved
POWER_FLY = 174.34  # Watt INITIAL_DRONE_BATTERY_CAPACITY/(22.41*60)sec
# Flight time is 17.93 if 20% reserved.
POWER_TX = 5  # Watt
POWER_WRITE = 2.34375e-05  # per Kb 3V*0.2A=0.6W/ 25MBbps
POWER_READ = 7.8125e-06  # per Kb # 1V*0.2A=0.2W/ 25MBps
POWER_PROCESS_PACKET = 7.8125e-06 * 1500
