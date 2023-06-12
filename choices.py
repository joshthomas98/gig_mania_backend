GENRE_CHOICES = (
    ('Rock', 'Rock'),
    ('Pop', 'Pop'),
    ('Jazz', 'Jazz'),
    ('Country', 'Country'),
    ('Hip Hop', 'Hip Hop'),
    ('R&B', 'R&B'),
    ('Electronic', 'Electronic'),
    ('Classical', 'Classical'),
    ('Reggae', 'Reggae'),
    ('Metal', 'Metal'),
    ('Folk', 'Folk'),
    ('Blues', 'Blues'),
    ('World Music', 'World Music'),
)

UK_COUNTRY_CHOICES = (
    ('England', 'England'),
    ('Wales', 'Wales'),
    ('Scotland', 'Scotland'),
    ('Northern Ireland', 'Northern Ireland'),
)

UK_COUNTY_CHOICES = (
    ('England', (
        ('Bedfordshire', 'Bedfordshire'),
        ('Berkshire', 'Berkshire'),
        ('Bristol', 'Bristol'),
        ('Buckinghamshire', 'Buckinghamshire'),
        ('Cambridgeshire', 'Cambridgeshire'),
        ('Cheshire', 'Cheshire'),
        ('Cornwall', 'Cornwall'),
        ('Cumbria', 'Cumbria'),
        ('Derbyshire', 'Derbyshire'),
        ('Devon', 'Devon'),
        ('Dorset', 'Dorset'),
        ('Durham', 'Durham'),
        ('East Sussex', 'East Sussex'),
        ('Essex', 'Essex'),
        ('Gloucestershire', 'Gloucestershire'),
        ('Greater London', 'Greater London'),
        ('Greater Manchester', 'Greater Manchester'),
        ('Hampshire', 'Hampshire'),
        ('Herefordshire', 'Herefordshire'),
        ('Hertfordshire', 'Hertfordshire'),
        ('Isle of Wight', 'Isle of Wight'),
        ('Kent', 'Kent'),
        ('Lancashire', 'Lancashire'),
        ('Leicestershire', 'Leicestershire'),
        ('Lincolnshire', 'Lincolnshire'),
        ('Merseyside', 'Merseyside'),
        ('Norfolk', 'Norfolk'),
        ('North Yorkshire', 'North Yorkshire'),
        ('Northamptonshire', 'Northamptonshire'),
        ('Northumberland', 'Northumberland'),
        ('Nottinghamshire', 'Nottinghamshire'),
        ('Oxfordshire', 'Oxfordshire'),
        ('Rutland', 'Rutland'),
        ('Shropshire', 'Shropshire'),
        ('Somerset', 'Somerset'),
        ('South Yorkshire', 'South Yorkshire'),
        ('Staffordshire', 'Staffordshire'),
        ('Suffolk', 'Suffolk'),
        ('Surrey', 'Surrey'),
        ('Tyne and Wear', 'Tyne and Wear'),
        ('Warwickshire', 'Warwickshire'),
        ('West Midlands', 'West Midlands'),
        ('West Sussex', 'West Sussex'),
        ('West Yorkshire', 'West Yorkshire'),
        ('Wiltshire', 'Wiltshire'),
        ('Worcestershire', 'Worcestershire'),
    )),
    ('Wales', (
        ('Blaenau Gwent', 'Blaenau Gwent'),
        ('Bridgend', 'Bridgend'),
        ('Caerphilly', 'Caerphilly'),
        ('Cardiff', 'Cardiff'),
        ('Carmarthenshire', 'Carmarthenshire'),
        ('Ceredigion', 'Ceredigion'),
        ('Conwy', 'Conwy'),
        ('Denbighshire', 'Denbighshire'),
        ('Flintshire', 'Flintshire'),
        ('Gwynedd', 'Gwynedd'),
        ('Isle of Anglesey', 'Isle of Anglesey'),
        ('Merthyr Tydfil', 'Merthyr Tydfil'),
        ('Monmouthshire', 'Monmouthshire'),
        ('Neath Port Talbot', 'Neath Port Talbot'),
        ('Newport', 'Newport'),
        ('Pembrokeshire', 'Pembrokeshire'),
        ('Powys', 'Powys'),
        ('Rhondda Cynon Taff', 'Rhondda Cynon Taff'),
        ('Swansea', 'Swansea'),
        ('Torfaen', 'Torfaen'),
        ('Vale of Glamorgan', 'Vale of Glamorgan'),
        ('Wrexham', 'Wrexham'),
    )),
    ('Scotland', (
        ('Aberdeen City', 'Aberdeen City'),
        ('Aberdeenshire', 'Aberdeenshire'),
        ('Angus', 'Angus'),
        ('Argyll and Bute', 'Argyll and Bute'),
        ('Clackmannanshire', 'Clackmannanshire'),
        ('Dumfries and Galloway', 'Dumfries and Galloway'),
        ('Dundee City', 'Dundee City'),
        ('East Ayrshire', 'East Ayrshire'),
        ('East Dunbartonshire', 'East Dunbartonshire'),
        ('East Lothian', 'East Lothian'),
        ('East Renfrewshire', 'East Renfrewshire'),
        ('Edinburgh', 'Edinburgh'),
        ('Falkirk', 'Falkirk'),
        ('Fife', 'Fife'),
        ('Glasgow', 'Glasgow'),
        ('Highland', 'Highland'),
        ('Inverclyde', 'Inverclyde'),
        ('Midlothian', 'Midlothian'),
        ('Moray', 'Moray'),
        ('Na h-Eileanan Siar', 'Na h-Eileanan Siar'),
        ('North Ayrshire', 'North Ayrshire'),
        ('North Lanarkshire', 'North Lanarkshire'),
        ('Orkney Islands', 'Orkney Islands'),
        ('Perth and Kinross', 'Perth and Kinross'),
        ('Renfrewshire', 'Renfrewshire'),
        ('Scottish Borders', 'Scottish Borders'),
        ('Shetland Islands', 'Shetland Islands'),
        ('South Ayrshire', 'South Ayrshire'),
        ('South Lanarkshire', 'South Lanarkshire'),
        ('Stirling', 'Stirling'),
        ('West Dunbartonshire', 'West Dunbartonshire'),
        ('West Lothian', 'West Lothian'),
    )),
    ('Northern Ireland', (
        ('Antrim', 'Antrim'),
        ('Armagh', 'Armagh'),
        ('Down', 'Down'),
        ('Fermanagh', 'Fermanagh'),
        ('Londonderry', 'Londonderry'),
        ('Tyrone', 'Tyrone'),
    )),
)

GIGGING_DISTANCE = (
    ('England', (
        ('South East', 'South East'),
        ('South West', 'South West'),
        ('London', 'London'),
        ('East of England', 'East of England'),
        ('West Midlands', 'West Midlands'),
        ('East Midlands', 'East Midlands'),
        ('Yorkshire and the Humber', 'Yorkshire and the Humber'),
        ('North West', 'North West'),
        ('North East', 'North East'),
    )),
    ('Scotland', (
        ('Highlands and Islands', 'Highlands and Islands'),
        ('North East Scotland', 'North East Scotland'),
        ('Central Belt', 'Central Belt'),
        ('South West Scotland', 'South West Scotland'),
    )),
    ('Wales', (
        ('North Wales', 'North Wales'),
        ('Mid Wales', 'Mid Wales'),
        ('South West Wales', 'South West Wales'),
        ('South East Wales', 'South East Wales'),
    )),
    ('Northern Ireland', (
        ('Antrim Coast and Glens', 'Antrim Coast and Glens'),
        ('Belfast', 'Belfast'),
        ('The Causeway Coast', 'The Causeway Coast'),
        ('County Armagh', 'County Armagh'),
        ('County Down', 'County Down'),
        ('Fermanagh Lakelands', 'Fermanagh Lakelands'),
        ('Lough Neagh', 'Lough Neagh'),
        ('Sperrin Mountains', 'Sperrin Mountains'),
        ('The Mournes', 'The Mournes'),
    )),
    ('All Counties', (
        ('Nationwide', 'Nationwide'),
    )),
)

ACT_TYPES = (
    ('Original Music', 'Original Music'),
    ('Covers', 'Covers'),
    ('Both', 'Both'),
)

ARTIST_TYPES = (
    ('Full band', 'Full band'),
    ('Solo artist', 'Solo artist'),
    ('Duo', 'Duo'),
)

GIGGING_DISTANCE = (
    ('England', (
        ('South East', 'South East'),
        ('South West', 'South West'),
        ('London', 'London'),
        ('East of England', 'East of England'),
        ('West Midlands', 'West Midlands'),
        ('East Midlands', 'East Midlands'),
        ('Yorkshire and the Humber', 'Yorkshire and the Humber'),
        ('North West', 'North West'),
        ('North East', 'North East'),
    )),
    ('Scotland', (
        ('Highlands and Islands', 'Highlands and Islands'),
        ('North East Scotland', 'North East Scotland'),
        ('Central Belt', 'Central Belt'),
        ('South West Scotland', 'South West Scotland'),
    )),
    ('Wales', (
        ('North Wales', 'North Wales'),
        ('Mid Wales', 'Mid Wales'),
        ('South West Wales', 'South West Wales'),
        ('South East Wales', 'South East Wales'),
    )),
    ('Northern Ireland', (
        ('Antrim Coast and Glens', 'Antrim Coast and Glens'),
        ('Belfast', 'Belfast'),
        ('The Causeway Coast', 'The Causeway Coast'),
        ('County Armagh', 'County Armagh'),
        ('County Down', 'County Down'),
        ('Fermanagh Lakelands', 'Fermanagh Lakelands'),
        ('Lough Neagh', 'Lough Neagh'),
        ('Sperrin Mountains', 'Sperrin Mountains'),
        ('The Mournes', 'The Mournes'),
    )),
    ('All Regions', (
        ('Nationwide', 'Nationwide'),
    )),
)

USER_TYPES = (
    ('Artist', 'Artist'),
    ('Venue', 'Venue'),
)
