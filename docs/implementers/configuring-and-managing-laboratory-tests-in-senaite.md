# Configuring and Managing Laboratory Tests in SENAITE

## Create Laboratory Departments

1. Navigate to:
    ◦ Setup → Departments
2. Create departments eg: Blood, Urine, Stool, etc

## Create Sample Types

1. Navigate to:
    ◦ Setup → Sample Types
2. Create sample type eg: Blood, Urine, Stool, etc. Note: Ensure the sample types match the expected test requirements.

## Create Analysis Categories

Analysis categories are used to group related laboratory tests.
1. Navigate to:
    ◦ Setup → Analysis Categories
2. Create categories such as: Blood, Urine, Skin, Sputum, etc. Ensure categories align with the laboratory workflow.

## Create Analysis Services (Tests)

Analysis Services represent laboratory tests.
1. Navigate to:
    ◦ Setup → Analysis Services
2. Create tests e.g: Complete Blood Count, Malaria Test, Blood Glucose, etc. The UUID of the Analysis Service in SENAITE must match the UUID of the corresponding laboratory test in the EMR/OpenMRS

## Create Analysis Templates

Analysis Templates define reusable testing structures.
1. Navigate to:
    ◦ Setup → Analysis Templates
2. Create analysis templates. The Analysis Template description should be the UUID of the corresponding Analysis Service.

## Create Analysis Profiles

This groups multiple analysis services into predefined panels.
1. Navigate to:
    ◦ Setup → Analysis Profiles
2. Create profiles eg: Complete Blood Count, Malaria Tests, etc
3. Add the required analysis services to each profile.      

## Export SENAITE Configuration and Add to Distro

1. Export **SENAITE: Export Content Structure** configs at http://localhost:8081/senaite/portal_setup/manage_exportSteps
2. Add the data.tar.gz file in the initializer configuration directory of the distro.