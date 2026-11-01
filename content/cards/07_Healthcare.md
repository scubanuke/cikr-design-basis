# Healthcare and Public Health

**So what?** A hospital makes nothing itself, and its emergency department must screen everyone who arrives. It runs on power, water and communications from elsewhere, so the design asks that it keep life-sustaining care going on its own, for a stated time, when those fail.

**Depends on:** Water, Energy, Communications, Transportation, Chemical
**Depended on by:** Emergency Services

## Sector framework — Healthcare and Public Health Sector Framework (DBA-HPH_Sector_Framework)
A sector framework states what a sector's systems must be built to withstand, from ordinary failures up to deliberate military action. This one covers the delivery of care, the supply of medical materials, and public health and laboratory work. It points out that a hospital produces no physical goods: its care depends on electric power, clean and dialysis-grade water, communications and medical gas that come from other sectors, and for the most time-critical patients their loss is measured in hours. It notes that existing rules measure readiness by plans and drills, and that no document yet states what care must be shown able to withstand.
*Source: DBA-HPH_Sector_Framework_v0_6*

## Facility class — Care Delivery (DBA-HPH-CD-FC1)
A facility class takes the sector framework down to one kind of facility. This one is mainly the hospital, with dialysis and long-term care also in its scope. It holds people who cannot leave and runs on power, water, gas and communications from outside. The class names two dangers: losing care for patients already inside, and a surge larger than the hospital can carry through to definitive care, measured by critically injured patients per hour, not by beds. It asks whether a hospital can hold life-sustaining care on its own, and it declares that a direct strike can destroy any part of a hospital, and that a campaign outlasting its endurance ends its continuity.
*Source: DBA-HPH-CD-FC1_Care_Delivery_v0_2*

## Use case — A Mass-Casualty Surge During a Grid and Communications Outage (DBA-HPH-UC-1)
A use case runs a postulated attack forward through a facility class to see where the design holds and where it does not. Here a capable adversary denies a region its electric grid and public communications, and a mass-casualty event sends many injured to a community hospital and a trauma center with no warning. The case shows the design largely holds: hospitals that triage at the door and plan for patients arriving without notice can receive them when no call comes. It also finds gaps: the class does not yet say what surge power capacity is needed, how staff are recalled when no message can be sent, or by what path patient counts are reported. This document is available to defenders and regulators on request.
*Source: DBA-HPH-UC-1_Surge_During_Grid_and_Communications_Outage_v0_1*

## Reference event — Loss of Power at Memorial Medical Center (DBA-HPH-RE-2)
A reference event reads a real event back through the design basis to ask whether the method was sufficient. During Hurricane Katrina in August 2005, Memorial Medical Center in New Orleans lost its power. The hospital stood below sea level, a 2004 warning about flooding had not been acted on, and its plan assumed backup power would last three days; it lasted less than two. Evacuation, including from a long-unused helipad, continued until the evening of 1 September. Experts in later litigation disagree on why the power failed. None of the four marks of military action was present. Read against the event, the hospital class held, with gaps, and nothing in the event fell outside it.
*Source: DBA-HPH-RE-2_Loss_of_Power_at_Memorial_Medical_Center_v0_1*
