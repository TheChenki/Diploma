from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField


# добавить BasementFullArea + GrLivArea

class HouseForm(FlaskForm):
    lot_frontage = IntegerField('Linear feet of street connected to property', default=1) ############################################

    lot_area = IntegerField('Lot size in square feet', default=1) ############################################

    street = SelectField('Type of road access to property', choices=[('0', 'Gravel'), ('1', 'Paved')]) ############################################

    alley = SelectField('Type of alley access to property', choices=[('1', 'Gravel'), ('2', 'Paved')]) ############################################

    lot_shape = SelectField('General shape of property', choices=[('0', 'Regular'), ('1', 'Slightly irregular'), ('2', 'Moderately irregular'), ('3', 'Irregular')]) ############################################

    land_contour = SelectField('Flatness of the property', choices=[('0', 'Near Flat/Level'), ('1', 'Banked'), ('2', 'Hillside'), ('3', 'Depression')]) ############################################

    utilities = SelectField('Type of utilities available', choices=[('0', 'Electricity, gas, water, sewer'), ('1', 'Electricity, gas, water, septic tank'),
                                                                    ('2', 'Electricity and gas only'), ('3', 'Electricity only')])

    lot_config = SelectField('Lot configuration', choices=[('0', 'Inside lot'), ('1', 'Corner lot'), ('2', 'Cul-de-sac'), ############################################
                                                           ('3', 'Frontage on 2 sides of property'), ('4', 'Frontage on 3 sides of property')]) #==================================

    land_slope = SelectField('Land slope', choices=[('0', 'Gentle slope'), ('1', 'Moderate Slope'), ('2', 'Severe Slope')]) ############################################

    neighborhood = SelectField('Physical locations within city limits', choices=[('0', 'Bloomington Heights'), ('1', 'Bluestem'), ('2', 'Briardale'),
                                                                                 ('3', 'Brookside'), ('4', 'Clear Creek'), ('5', 'College Creek'),
                                                                                 ('6', 'Crawford'), ('7', 'Edwards'), ('8', 'Gilbert'),
                                                                                 ('9', 'Iowa DOT and Rail Road'), ('10', 'Meadow Village'), ('11', 'Mitchell'),
                                                                                 ('12', 'North Ames'), ('13', 'Northridge'), ('14', 'Northpark Villa'),
                                                                                 ('15', 'Northridge Heights'), ('16', 'Northwest Ames'), ('17', 'Old Town'),
                                                                                 ('18', 'South & West of Iowa State University'), ('19', 'Sawyer'), ('20', 'Sawyer West'),
                                                                                 ('21', 'Somerset'), ('22', 'Stone Brook'), ('23', 'Timberland'), ('24', 'Veenker')])

    building_type = SelectField('Type of dwelling', choices=[('0', 'Single-family Detached'), ('1', 'Two-family Conversion'),
                                                             ('2', 'Duplex'), ('3', 'Townhouse End Unit'),
                                                             ('4', 'Townhouse Inside Unit')])

    house_style = SelectField('Style of dwelling', choices=[('0', 'One story'), ('1', 'One and one-half story'), #################
                                                           ('3', 'Two story'), ('4', 'Two and one-half story'),
                                                           ('6', 'Split Foyer'), ('7', 'Split Level')])

    overall_quality = SelectField('Quality of materials and house finish', choices=[('10', 'Very Excellent'), ('9', 'Excellent'), ('8', 'Very Good'), ('7', 'Good'),
                                                                                    ('6', 'Above Average'), ('5', 'Average'), ('4', 'Below Average'), ('3', 'Fair'),
                                                                                    ('2', 'Poor'), ('1', 'Very Poor')])

    overall_condition = SelectField('Overall condition of the house', choices=[('10', 'Very Excellent'), ('9', 'Excellent'), ('8', 'Very Good'), ('7', 'Good'),
                                                                               ('6', 'Above Average'), ('5', 'Average'), ('4', 'Below Average'), ('3', 'Fair'),
                                                                               ('2', 'Poor'), ('1', 'Very Poor')])

    year_build = IntegerField('Original construction date', default=1)

    year_remodel = IntegerField('Remodel date', default=1)

    roof_style = SelectField('Type of roof', choices=[('0', 'Flat'), ('1', 'Gable'), ('2', 'Barn'), ('3', 'Hip'), ('4', 'Mansard'), ('5', 'Shed')])

    roof_material = SelectField('Roof material', choices=[('0', 'Clay/Tile'), ('1', 'Standart/Composite shingle'), ('2', 'Membrane'), ('3', 'Metal'), ('4', 'Roll'), ('5', 'Gravel & Tar'),
                                                         ('6', 'Gravel & Tar'), ('7', 'Wood Shakes'), ('8', 'Wood Shingles')])

    exterior_first = SelectField('Exterior covering on house (First material)', choices=[('0', 'Asbestos Shingles'), ('1', 'Asphalt Shingles'), ('2', 'Brick Common'),
                                                                                         ('3', 'Brick Face'), ('4', 'Cinder Block'), ('5', 'Cement Board'),
                                                                                         ('6', 'Hard Board'), ('7', 'Imitation Stucco'), ('8', 'Metal Siding'),
                                                                                         ('9', 'Other'), ('10', 'Plywood'), ('11', 'Precast'),
                                                                                         ('12', 'Stone'), ('13', 'Stucco'), ('14', 'Vinyl Siding'),
                                                                                         ('15', 'Wood Siding'), ('16', 'Wood Shingles')])

    exterior_second = SelectField('Exterior covering on house (Second material)', choices=[('0', 'Asbestos Shingles'), ('1', 'Asphalt Shingles'), ('2', 'Brick Common'),
                                                                                           ('3', 'Brick Face'), ('4', 'Cinder Block'), ('5', 'Cement Board'),
                                                                                           ('6', 'Hard Board'), ('7', 'Imitation Stucco'), ('8', 'Metal Siding'),
                                                                                           ('9', 'Other'), ('10', 'Plywood'), ('11', 'Precast'),
                                                                                           ('12', 'Stone'), ('13', 'Stucco'), ('14', 'Vinyl Siding'),
                                                                                           ('15', 'Wood Siding'), ('16', 'Wood Shingles')])

    masonry_veneer_type = SelectField('Masonry veneer type', choices=[('0', 'Brick Common'), ('1', 'Brick Face'), ('2', 'Cinder Block'), ('3', 'None'), ('4', 'Stone')])

    masonry_veneer_area = IntegerField('Masonry veneer area', default=1)

    exterior_quality = SelectField('Quality of the material on the exterior', choices=[('0', 'Excellent'), ('1', 'Good'), ('2', 'Average/Typical'), ('3', 'Fair'), ('4', 'Poor')])

    exterior_condition = SelectField('Condition of the material on the exterior', choices=[('0', 'Excellent'), ('1', 'Good'), ('2', 'Average/Typical'), ('3', 'Fair'), ('4', 'Poor')])

    foundation = SelectField('Type of foundation', choices=[('0', 'Brick & Tile'), ('1', 'Cinder block'), ('2', 'Poured concrete'), ('3', 'Slab'), ('4', 'Stone'), ('5', 'Wood')])

    basement_quality = SelectField('Height of the basement', choices=[('0', '100+ inches'), ('1', '90-99 inches'), ('2', '80-89 inches'), ('3', '70-79 inches'), ('4', '<70 inches'), ('5', 'No basement')])

    basement_condition = SelectField('Condition of the basement', choices=[('0', 'Excellent'), ('1', 'Good'), ('2', 'Average/Typical'), ('3', 'Fair'), ('4', 'Poor'), ('5', 'No basement')])

    basement_exposure = SelectField('Basement exposure', choices=[('0', 'Good Exposure'), ('1', 'Average Exposure'), ('2', 'Minimum Exposure'), ('3', 'No Exposure'), ('4', 'No basement')])

    basement_type_1 = SelectField('First basement finished area type', choices=[('0', 'Good Living Quarters'), ('1', 'Average Living Quarters'), ('2', 'Below Average Living Quarters'),
                                                                          ('3', 'Average Rec Room'), ('4', 'Low Quality'), ('5', 'Unfinshed'), ('6', 'No Basement')])

    basement_finished_area_1 = IntegerField('First basement finished area square feet', default=1)

    basement_type_2 = SelectField('Second basement finished area type', choices=[('0', 'Good Living Quarters'), ('1', 'Average Living Quarters'), ('2', 'Below Average Living Quarters'),
                                                                          ('3', 'Average Rec Room'), ('4', 'Low Quality'), ('5', 'Unfinshed'), ('6', 'No Basement')])

    basement_finished_area_2 = IntegerField('Second basement finished area square feet', default=1)

    basement_unfinished_area = IntegerField('Basement unfinished area square feet', default=1)

    heating_type = SelectField('Type of heating', choices=[('0', 'Floor'), ('1', 'Gas forced warm air furnace'), ('2', 'Gas hot water or steam heat'),
                                                           ('3', 'Gravity furnace'), ('4', 'Hot water or steam heat other than gas'), ('5', 'Wall furnace')])

    heating_quality = SelectField('Heating quality and condition', choices=[('0', 'Excellent'), ('1', 'Good'), ('2', 'Average/Typical'),
                                                                            ('3', 'Fair'), ('4', 'Poor')])

    central_air = SelectField('Central air conditioning', choices=[('0', 'No'), ('1', 'Yes')])

    electrical = SelectField('Electrical system', choices=[('0', 'No electrical system'), ('1', 'Standard Circuit Breakers & Romex'), ('2', 'Fuse Box over 60 AMP and all Romex wiring (Average)'),
                                                           ('3', '60 AMP Fuse Box and mostly Romex wiring (Fair)'), ('4', '60 AMP Fuse Box and mostly knob & tube wiring (poor)'), ('5', 'Mixed')])

    first_floor_area = IntegerField('First floor square feet', default=1)

    second_floor_area = IntegerField('Second Floor square feet', default=0)

    lq_finished_area = IntegerField('Low quality finished square feet (all floors)', default=0)

    basement_full_bath = IntegerField('Basement full bathrooms', default=0)

    basement_half_bath = IntegerField('Basement half bathrooms', default=0)

    full_bath = IntegerField('Full bathrooms above grade', default=0)

    half_bath = IntegerField('Half bathrooms above grade', default=0)

    bedrooms = IntegerField('Bedrooms above grade', default=0)

    kitchens = IntegerField('Kitchens above grade', default=0)

    kitchen_quality = SelectField('Kitchen quality', choices=[('0', 'Excellent'), ('1', 'Good'), ('2', 'Average/Typical'),
                                                              ('3', 'Fair'), ('4', 'Poor')])

    total_rooms = IntegerField('Total rooms above grade (does not include bathrooms)', default=0)

    functionality = SelectField('Home functionality', choices=[('0', 'Typical'), ('1', 'Minor Deductions 1'), ('2', 'Minor Deductions 2'),
                                                              ('3', 'Moderate Deductions'), ('4', 'Major Deductions 1'), ('5', 'Major Deductions 2'),
                                                              ('5', 'Severely Damaged'), ('5', 'Salvage only'), ('5', 'Major Deductions 2')])

    fireplaces = IntegerField('Number of fireplaces', default=0)

    fireplace_quality = SelectField('Fireplace quality', choices=[('0', 'No fireplace'), ('1', 'Exceptional Masonry Fireplace'), ('2', 'Masonry Fireplace in main level'),
                                                                  ('3', 'Prefabricated Fireplace in main living area or Masonry Fireplace in basement'), ('4', 'Prefabricated Fireplace in basement'),
                                                                  ('5', 'Ben Franklin stove')])

    garage_type = SelectField('Garage location', choices=[('0', 'No garage'), ('1', 'More than one type of garage'), ('2', 'Attached to home'),
                                                          ('3', 'Basement Garage'), ('4', 'Built-In (Garage part of house - typically has room above garage)'),
                                                          ('5', 'Detached from home')])

    garage_year = IntegerField('Year garage was built', default=0)

    garage_finish = SelectField('Interior finish of the garage', choices=[('0', 'No Garage'), ('1', 'Finished'), ('2', 'Rough Finished'),
                                                                          ('3', 'Unfinished')])

    garage_cars = IntegerField('Size of garage in car capacity', default=0)

    garage_area = IntegerField('Size of garage in square feet', default=0)

    garage_quality = SelectField('Garage quality', choices=[('0', 'No Garage'), ('1', 'Excellent'), ('2', 'Good'), ('3', 'Average/Typical'),
                                                             ('4', 'Fair'), ('5', 'Poor')])

    garage_condition = SelectField('Garage condition', choices=[('0', 'No Garage'), ('1', 'Excellent'), ('2', 'Good'),
                                                                ('3', 'Average/Typical'),
                                                                ('4', 'Fair'), ('5', 'Poor')])

    paved_drive = SelectField('Paved driveway', choices=[('0', 'Paved'), ('1', 'Partial Pavement'), ('2', 'Dirt/Gravel')])

    wood_deck_area = IntegerField('Wood deck area in square feet', default=0)

    open_porch_area = IntegerField('Open porch area in square feet', default=0)

    enclosed_porch = IntegerField('Enclosed porch area in square feet', default=0)

    three_season_porch_area = IntegerField('Three season porch area in square feet', default=0)

    screen_porch_area = IntegerField('Screen porch area in square feet', default=0)

    pool_area = IntegerField('Pool area in square feet', default=0)

    pool_quality = SelectField('Garage condition', choices=[('0', 'No pool'), ('1', 'Excellent'), ('2', 'Good'),
                                                            ('3', 'Average/Typical'),
                                                            ('4', 'Fair'), ('5', 'Poor')])

    fence = SelectField('Fence quality', choices=[('0', 'No Fence'), ('1', 'Good Privacy'), ('2', 'Minimum Privacy'),
                                                  ('3', 'Good Wood'), ('4', 'Minimum Wood/Wire')])

    misc_feature = SelectField('Miscellaneous feature not covered in other categories', choices=[('0', 'None'), ('1', 'Elevator'), ('2', '2nd Garage'),
                                                                                                 ('3', 'Other'), ('4', 'Shed (over 100 SF)'), ('5', 'Tennis Court')])

    misc_value = IntegerField('Value of miscellaneous feature', default=0)

