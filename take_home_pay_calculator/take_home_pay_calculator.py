# Globals 
PERSONAL_ALLOWANCE_THRESHOLD = 12570        # Up to £12,570
BASIC_RATE_THRESHOLD = 50270                # Between £12,570 and £50,270
HIGHER_RATE_THRESHOLD = 150000              # Between £50,270 and £150,000
ADDITIONAL_RATE_THRESHOLD = 150000          # Over £150,000
PERSONAL_ALLOWANCE_PERCENT = 0              # 0% tax on salary under £12,570
BASIC_RATE_PERCENT = 0.2                    # 20% tax on salary between £12,570 and £50,270
HIGHER_RATE_PERCENT = 0.4                   # 40% tax on salary between £50,270 and £150,000
ADDITIONAL_RATE_PRECENT = 0.45              # 45% tax on salary over £150,000

NI_LOWER_THRESHOLD  = 12584                 # Only pay NI if you earn over £12,584 per year (£242 pw)
NI_HIGHER_THRESHOLD = 50270                 # Under £50,270 = 12& over £50,270 = 2%

NI_RATE_PERCENT_UNDER_HT = 0.12             # 12% NI on salary under £50,270
NI_RATE_PERCENT_OVER_HT = 0.02              # 2%  NI on salary over  £50,270


# Functions
def pension_payable(salary: float, pays_pension_contributions: str, pension_contributions_percent: float) -> float:
    """
    This function calculates the amount the user will pay into their pension
    :param salary: The users yearly gross salary
    :param pays_pension: The users answer to the question (Y/N)
    :return: float, the amount of pension the users pays
    """
    if pays_pension_contributions.upper() == "Y":
        pension_contributions = salary * (pension_contributions_percent / 100)
    else:
        pension_contributions = 0 
    return pension_contributions


def tax_payable(salary: float) -> float:
    """
    This function returns the tax deduction on the salary
    :param salary: The users yearly gross salary
    :return: float, the amount of tax the user pays
    """
    pension_deductions = pension_payable(salary, pays_pension_contributions, pension_contributions_percent)
    taxable_salary = salary - pension_deductions
    if salary < PERSONAL_ALLOWANCE_THRESHOLD: 
        tax_deduction = 0
    elif salary < BASIC_RATE_THRESHOLD:
        taxable_income = taxable_salary - PERSONAL_ALLOWANCE_THRESHOLD
        tax_deduction = (taxable_income * BASIC_RATE_PERCENT) 
    elif salary < HIGHER_RATE_THRESHOLD:
        salary_over_higher_rate = salary - BASIC_RATE_THRESHOLD 
        basic_rate_taxable = salary - salary_over_higher_rate - PERSONAL_ALLOWANCE_THRESHOLD
        higher_rate_taxable = taxable_salary - BASIC_RATE_THRESHOLD 
        tax_deduction = (basic_rate_taxable * BASIC_RATE_PERCENT) + (higher_rate_taxable * HIGHER_RATE_PERCENT) 
    elif salary > ADDITIONAL_RATE_THRESHOLD:
        salary_over_additional_rate = salary - ADDITIONAL_RATE_THRESHOLD
        basic_rate_taxable = BASIC_RATE_THRESHOLD - PERSONAL_ALLOWANCE_THRESHOLD
        higher_rate_taxable = HIGHER_RATE_THRESHOLD - BASIC_RATE_THRESHOLD
        additional_rate_taxable = salary_over_additional_rate - ADDITIONAL_RATE_THRESHOLD
        tax_deduction = (basic_rate_taxable * BASIC_RATE_PERCENT) + (higher_rate_taxable * HIGHER_RATE_PERCENT) + (additional_rate_taxable * ADDITIONAL_RATE_PRECENT)
    return tax_deduction


def national_insurance_payable(salary: float, pension_payable: float) -> float:
    """
    This function returns the national insurance deduction on the salary
    :param salary: The users yearly gross salary
    :param pension_payable: The pension contributions, to be deducted before national insurance 
    :return: float, the amount of national insurance the user pays
    """
    pension_deductions = pension_payable(salary, pays_pension_contributions, pension_contributions_percent)
    taxable_salary = salary - pension_deductions
    if salary < NI_LOWER_THRESHOLD:
        national_insurance_deductions = 0
    elif salary < NI_HIGHER_THRESHOLD:
        taxable_salary = taxable_salary - NI_LOWER_THRESHOLD
        national_insurance_deductions = taxable_salary * NI_RATE_PERCENT_UNDER_HT
    elif salary > NI_HIGHER_THRESHOLD:
        salary_over_NI_higher_rate = taxable_salary - NI_HIGHER_THRESHOLD
        salary_over_NI_lower_rate = taxable_salary - salary_over_NI_higher_rate - NI_LOWER_THRESHOLD
        lower_rate_taxable = salary_over_NI_lower_rate * NI_RATE_PERCENT_UNDER_HT
        higher_rate_taxable = salary_over_NI_higher_rate * NI_RATE_PERCENT_OVER_HT 
        national_insurance_deductions = lower_rate_taxable + higher_rate_taxable
    return national_insurance_deductions


def annual_take_home_salary(salary: float, pension_payable: float, tax_payable: float, national_insurance_payable: float) -> float:
    """
    This function returns the annual take home salary
    :param salary: The users yearly gross salary
    :param pension_payable: The annual pension contributions, to be deducted
    :param tax_payable: The annual tax deductions, to be deducted
    :param national_insurance_payable: The annual national insurance deductions, to be deducted
    :return: float, The users annual take home salary
    """
    annual_pension_payable = pension_payable(salary, pays_pension_contributions, pension_contributions_percent)
    annual_tax_payable = tax_payable(salary)
    annual_national_insurance_payable = national_insurance_payable(salary, pension_payable)
    annual_take_home_salary = salary - annual_pension_payable - annual_tax_payable - annual_national_insurance_payable
    return annual_take_home_salary


def monthly_take_home_salary(salary: float, annual_take_home_salary: float) -> float:
    """
    This function returns the monthly take home salary
    :param salary: The users yearly gross salary
    :param annual_take_home_salary: 
    :return: float, The users monthly take home salary
    """
    monthly_take_home_salary = annual_take_home_salary(salary, pension_payable, tax_payable, national_insurance_payable) / 12 # annual take home divided by 12 to give montlhy take home
    return monthly_take_home_salary


def weekly_take_home_salary(salary: float, annual_take_home_salary: float) -> float:
    """
    This function returns the weekly take home salary
    :param salary: The users yearly gross salary
    :param annual_take_home_salary: 
    :return: float, The users weekly salary
    """
    weekly_take_home_salary = annual_take_home_salary(salary, pension_payable, tax_payable, national_insurance_payable) / 52 # annual take home divided by 52 to give weekly take home
    return weekly_take_home_salary


# Variables
salary = 65000                           # Enter your yearly gross salary
pays_pension_contributions = "Y"         # Enter Y/N 
pension_contributions_percent = 5        # Enter percentage of pension contributions


# Main code
def main():
    # Salary 
    annual_take_home = annual_take_home_salary(salary, pension_payable, tax_payable, national_insurance_payable)
    monthly_take_home = monthly_take_home_salary(salary, annual_take_home_salary)
    weekly_take_home = weekly_take_home_salary(salary, annual_take_home_salary)
    formatted_annual_take_home = "{:.2f}".format(annual_take_home)     # Limits the output to 2 decimal places
    formatted_monthly_take_home = "{:.2f}".format(monthly_take_home)   # Limits the output to 2 decimal places
    formatted_weekly_take_home = "{:.2f}".format(weekly_take_home)     # Limits the output to 2 decimal places
    # Deductions
    annual_tax_deductions = tax_payable(salary)
    annual_national_insurance_deductions = national_insurance_payable(salary, pension_payable)
    annual_pension_contributions = pension_payable(salary, pays_pension_contributions, pension_contributions_percent)
    formatted_annual_tax_deductions = "{:.2f}".format(annual_tax_deductions)
    formatted_annual_national_insurance_deductions = "{:.2f}".format(annual_national_insurance_deductions)
    formatted_annual_pension_contributions = "{:.2f}".format(annual_pension_contributions)
    # Print statements
    print("Annual take home salary: £" + str(formatted_annual_take_home))
    print("Monthly take home salary: £" + str(formatted_monthly_take_home))
    print("Weekly take home salary: £" + str(formatted_weekly_take_home))
    print("Annual tax deduction: £" + str(formatted_annual_tax_deductions))
    print("Annual national insurance deductions: £" + str(formatted_annual_national_insurance_deductions))
    print("Annual pension contributions: £" + str(formatted_annual_pension_contributions))


if __name__ == "__main__":
    main()
