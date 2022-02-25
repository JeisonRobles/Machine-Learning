SELECT
	upper(NAME_EDUCATION_TYPE) as 'EDUCATION',
	upper(NAME_FAMILY_STATUS) as 'FAMILY STATUS',
	upper(NAME_INCOME_TYPE) AS 'INCOME TYPE',
	credit_record.STATUS as 'STATUS',
	'ID:  '||credit_record.ID || '  ,Total income:  ' || application_record.AMT_INCOME_TOTAL as 'Income per ID'
FROM
	application_record

INNER JOIN 
	credit_record
ON
	application_record.ID = credit_record.ID
	
WHERE
	NAME_INCOME_TYPE = 'Working'
-- 	STATUS = 'C'
	
	
LIMIT 10