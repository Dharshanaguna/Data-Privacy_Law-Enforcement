def get_masking_technique(attribute):
    attribute_mappings = {
        'DISTRICTNAME': 'Hashing',
        'UNITNAME': 'Hashing',
        'Crime_No': 'Hashing',
        'Year': 'Time Aggregation',
        'RI': 'Hashing',
        'Noofvehicle_involved': 'Random Noise Addition',
        'Accident_Classification': 'Category Generalization',
        'Accident_Spot': 'Location Aggregation',
        'Accident_Location': 'Location Aggregation',
        'Accident_SubLocation': 'Location Aggregation',
        'Accident_SpotB': 'Location Aggregation',
        'Main_Cause': 'Category Generalization',
        'Hit_Run': 'Boolean Masking',
        'Severity': 'Category Generalization',
        'Collision_Type': 'Category Generalization',
        'Junction_Control': 'Category Generalization',
        'Road_Character': 'Category Generalization',
        'Road_Type': 'Category Generalization',
        'Surface_Type': 'Category Generalization',
        'Surface_Condition': 'Category Generalization',
        'Road_Condition': 'Category Generalization',
        'Weather': 'Category Generalization',
        'Lane_Type': 'Category Generalization',
        'Road_Markings': 'Category Generalization',
        'Spot_Conditions': 'Category Generalization',
        'Side_Walk': 'Boolean Masking',
        'RoadJunction': 'Category Generalization',
        'Collision_TypeB': 'Category Generalization',
        'Accident_Road': 'Location Aggregation',
        'Landmark_first': 'Location Aggregation',
        'landmark_second': 'Location Aggregation',
        'Distance_LandMark_First': 'Random Noise Addition',
        'Distance_LandMark_Second': 'Random Noise Addition',
        'Accident_Description': 'Text Redaction',
        'Latitude': 'Geographic Masking',
        'Longitude': 'Geographic Masking',
        'District_Name': 'Hashing',
        'UnitName': 'Hashing',
        'FIRNo': 'Hashing',
        'Month': 'Time Aggregation',
        'AccusedName': 'Name Masking',
        'Person_Name': 'Name Masking',
        'age': 'Age Binning',
        'Caste': 'Category Generalization',
        'Profession': 'Category Generalization',
        'Sex': 'Category Generalization',
        'PresentAddress': 'Address Masking',
        'PresentCity': 'Location Aggregation',
        'PresentState': 'Location Aggregation',
        'PermanentAddress': 'Address Masking',
        'PermanentCity': 'Location Aggregation',
        'PermanentState': 'Location Aggregation',
        'Nationality_Name': 'Category Generalization',
        'DOB': 'Date Generalization',
        'Person_No': 'Hashing',
        'Arr_ID': 'Hashing',
        'crime_no': 'Hashing',
        'Name': 'Name Masking',
        'Crime_No': 'Hashing',
        'Charge_Sheeted': 'Boolean Masking',
        'Charge_Sheet_Number': 'Hashing',
        'FIR_Date': 'Date Generalization',
        'Report_Date': 'Date Generalization',
        'Final_Report_Date': 'Date Generalization',
        'Report_Type': 'Category Generalization',
        'FIR_ID': 'Hashing',
        'Unit_ID': 'Hashing',
        'FR_ID': 'Hashing',
        'ComplainantName': 'Name Masking',
        'Relation': 'Category Generalization',
        'RelationshipName': 'Category Generalization',
        'DateOfBirth': 'Date Generalization',
        'Age': 'Age Binning',
        'Nationality': 'Category Generalization',
        'Occupation': 'Category Generalization',
        'Address': 'Address Masking',
        'City': 'Location Aggregation',
        'State': 'Location Aggregation',
        'Pincode': 'Postal Code Masking',
        'Religion': 'Category Generalization',
        'Complaint_ID': 'Hashing',
        'Offence_From_Date': 'Date Generalization',
        'Offence_To_Date': 'Date Generalization',
        'FIR_Reg_DateTime': 'Date Generalization',
        'FIR Type': 'Category Generalization',
        'FIR_Stage': 'Category Generalization',
        'Complaint_Mode': 'Category Generalization',
        'CrimeGroup_Name': 'Category Generalization',
        'CrimeHead_Name': 'Category Generalization',
        'ActSection': 'Text Redaction',
        'IOName': 'Name Masking',
        'KGID': 'Hashing',
        'IOAssigned_Date': 'Date Generalization',
        'Internal_IO': 'Boolean Masking',
        'Place of Offence': 'Location Aggregation',
        'Distance from PS': 'Random Noise Addition',
        'Beat_Name': 'Category Generalization',
        'Village_Area_Name': 'Location Aggregation',
        'Male': 'Age Binning',
        'Female': 'Age Binning',
        'Boy': 'Age Binning',
        'Girl': 'Age Binning',
        'Age 0': 'Age Binning',
        'VICTIM COUNT': 'Random Noise Addition',
        'Accused Count': 'Random Noise Addition',
        'Arrested Male': 'Age Binning',
        'Arrested Female': 'Age Binning',
        'Arrested Count\tNo.': 'Random Noise Addition',
        'Accused_ChargeSheeted Count': 'Random Noise Addition',
        'Conviction Count': 'Random Noise Addition',
        'Unit_Name': 'Hashing',
        'MOB_Number': 'Hashing',
        'MobOpenDate': 'Date Generalization',
        'MOB_Open_Year': 'Time Aggregation',
        'Arrested_By': 'Name Masking',
        'Grading': 'Category Generalization',
        'PS_Native': 'Location Aggregation',
        'PS_District': 'Location Aggregation',
        'Offender_Class': 'Category Generalization',
        'Brief_Fact': 'Text Redaction',
        'Present_WhereAbouts': 'Location Aggregation',
        'Gang_Strength': 'Random Noise Addition',
        'Ident_Officer': 'Name Masking',
        'officer_rank': 'Category Generalization',
        'Crime_Group1': 'Category Generalization',
        'Crime_Head2': 'Category Generalization',
        'class': 'Category Generalization',
        'AGE': 'Age Binning',
        'PresentAge': 'Age Binning',
        'Address': 'Address Masking',
        'SEX': 'Category Generalization',
        'Locality': 'Location Aggregation',
        'LastUpdatedDate': 'Date Generalization',
        'Rowdy_Sheet_No': 'Hashing',
        'AliasName': 'Name Masking',
        'RS_Open_Date': 'Date Generalization',
        'Rowdy_Classification_Details': 'Text Redaction',
        'Activities_Description': 'Text Redaction',
        'Rowdy_Category': 'Category Generalization',
        'PrevCase_Details': 'Text Redaction',
        'Father_Name': 'Name Masking',
        'Source_Of_Income': 'Category Generalization',
        'PresentWhereabout': 'Location Aggregation',
        'VictimName': 'Name Masking',
        'PersonType': 'Category Generalization',
        'InjuryType': 'Category Generalization',
        'Injury_Nature': 'Category Generalization',
        'Victim_ID': 'Hashing'

    }
    return attribute_mappings.get(attribute, 'Technique not specified')