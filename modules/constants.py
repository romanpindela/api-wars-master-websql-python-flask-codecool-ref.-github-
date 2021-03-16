# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      constants
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------- names compatible with external api -----------------------------------------

class _Subject:
    PEOPLE = 'people'
    PLANETS = 'planets'
    STARSHIPS = 'starships'
    VEHICLES = 'vehicles'


SUBJECT = _Subject()


class _Key:
    class Planets:
        CLIMATE = 'climate'
        DIAMETER = 'diameter'
        GRAVITY = 'gravity'
        NAME = 'name'
        ORBITAL = 'orbital_period'
        POPULATION = 'population'
        RESIDENTS = 'residents'
        ROTATION = 'rotation_period'
        TERRAIN = 'terrain'
        WATER = 'surface_water'

    class Starships:
        ATSP = 'max_atmosphering_speed'
        CARGO = 'cargo_capacity'
        CLASS = 'starship_class'
        CREW = 'crew'
        LENGTH = 'length'
        MANUFACTURER = 'manufacturer'
        MGLT = 'MGLT'
        MODEL = 'model'
        NAME = 'name'
        PASSENGERS = 'passengers'
        PILOTS = 'pilots'

    class Vehicles:
        ATSP = 'max_atmosphering_speed'
        CARGO = 'cargo_capacity'
        CLASS = 'vehicle_class'
        CREW = 'crew'
        LENGTH = 'length'
        MODEL = 'model'
        NAME = 'name'
        PASSENGERS = 'passengers'
        PILOTS = 'pilots'

    class People:
        BIRTH = 'birth_year'
        EYE = 'eye_color'
        GENDER = 'gender'
        HAIR = 'hair_color'
        HEIGHT = 'height'
        HOMEWORLD = 'homeworld'
        MASS = 'mass'
        NAME = 'name'
        PILOTED_STARSHIPS = 'starships'
        PILOTED_VEHICLES = 'vehicles'
        SKIN = 'skin_color'

    PLANETS = Planets()
    STARSHIPS = Starships()
    VEHICLES = Vehicles()
    PEOPLE = People()


KEY = _Key()


# ---------------------------------------------------- sort order -----------------------------------------------------

SUBJECT_ORDER = (
    SUBJECT.PLANETS,
    SUBJECT.STARSHIPS,
    SUBJECT.VEHICLES,
    SUBJECT.PEOPLE
)


class _Headers:
    PLANETS = (
        KEY.PLANETS.NAME,
        KEY.PLANETS.DIAMETER,
        KEY.PLANETS.CLIMATE,
        KEY.PLANETS.TERRAIN,
        KEY.PLANETS.WATER,
        KEY.PLANETS.ROTATION,
        KEY.PLANETS.ORBITAL,
        KEY.PLANETS.GRAVITY,
        KEY.PLANETS.POPULATION,
        KEY.PLANETS.RESIDENTS
    )
    STARSHIPS = (
        KEY.STARSHIPS.NAME,
        KEY.STARSHIPS.MODEL,
        KEY.STARSHIPS.CLASS,
        KEY.STARSHIPS.MANUFACTURER,
        KEY.STARSHIPS.CREW,
        KEY.STARSHIPS.PASSENGERS,
        KEY.STARSHIPS.CARGO,
        KEY.STARSHIPS.LENGTH,
        KEY.STARSHIPS.ATSP,
        KEY.STARSHIPS.MGLT,
        KEY.STARSHIPS.PILOTS
    )
    VEHICLES = (
        KEY.VEHICLES.NAME,
        KEY.VEHICLES.MODEL,
        KEY.VEHICLES.CLASS,
        KEY.VEHICLES.CREW,
        KEY.VEHICLES.PASSENGERS,
        KEY.VEHICLES.CARGO,
        KEY.VEHICLES.LENGTH,
        KEY.VEHICLES.ATSP,
        KEY.VEHICLES.PILOTS
    )
    PEOPLE = (
        KEY.PEOPLE.NAME,
        KEY.PEOPLE.BIRTH,
        KEY.PEOPLE.GENDER,
        KEY.PEOPLE.EYE,
        KEY.PEOPLE.HAIR,
        KEY.PEOPLE.SKIN,
        KEY.PEOPLE.HEIGHT,
        KEY.PEOPLE.MASS,
        KEY.PEOPLE.HOMEWORLD,
        KEY.PEOPLE.PILOTED_STARSHIPS,
        KEY.PEOPLE.PILOTED_VEHICLES
    )


HEADERS = _Headers()


# --------------------------------------------------- webside logic ---------------------------------------------------

# The names of the columns that contain the button data.
class _ColumnWithButton:
    PLANETS = (
        KEY.PLANETS.RESIDENTS,
    )
    STARSHIPS = (
        KEY.STARSHIPS.PILOTS,
    )
    VEHICLES = (
        KEY.VEHICLES.PILOTS,
    )
    PEOPLE = (
        KEY.PEOPLE.HOMEWORLD,
        KEY.PEOPLE.PILOTED_STARSHIPS,
        KEY.PEOPLE.PILOTED_VEHICLES
    )


COLUMN_WITH_BUTTON = _ColumnWithButton()


# The names of the columns that contain the subject data.
COLUMN_NAMES_WITH_PLANETS = ('homeworld'),
COLUMN_NAMES_WITH_PEOPLE = ('residents', 'pilots')


# -------------------------------------------------- data formatting --------------------------------------------------

# New names for the columns.
class _ColumnNewName:
    MGLT = 'Megalights'


COLUMN_NEW_NAME = _ColumnNewName()


# Data names are replaced in the formatting process.
class _FormatName:
    NO_WATER = 'no water'
    UNKNOWN = 'unknown'


FORMAT_NAME = _FormatName()
