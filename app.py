import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calculate_missing_value(start_date, end_date, lead_time, shipping, time_unit):
    try:
        if end_date == "":
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            if time_unit == "months":
                return start_date + relativedelta(months=int(lead_time) + int(shipping))
            elif time_unit == "weeks":
                return start_date + timedelta(weeks=int(lead_time) + int(shipping))
            elif time_unit == "days":
                return start_date + timedelta(days=int(lead_time) + int(shipping))
        elif start_date == "":
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            if time_unit == "months":
                return end_date - relativedelta(months=int(lead_time) + int(shipping))
            elif time_unit == "weeks":
                return end_date - timedelta(weeks=int(lead_time) + int(shipping))
            elif time_unit == "days":
                return end_date - timedelta(days=int(lead_time) + int(shipping))
        elif lead_time == "":
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            delta = relativedelta(end_date, start_date)
            if time_unit == "months":
                return (delta.years * 12 + delta.months) - int(shipping)
            elif time_unit == "weeks":
                return ((end_date - start_date).days // 7) - int(shipping)
            elif time_unit == "days":
                return (end_date - start_date).days - int(shipping)
        elif shipping == "":
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            delta = relativedelta(end_date, start_date)
            if time_unit == "months":
                return (delta.years * 12 + delta.months) - int(lead_time)
            elif time_unit == "weeks":
                return ((end_date - start_date).days // 7) - int(lead_time)
            elif time_unit == "days":
                return (end_date - start_date).days - int(lead_time)
        else:
            return "One field must be left blank!"
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("📅 Project Timeline Calculator")

start_date = st.text_input("Start Date (YYYY-MM-DD)", "")
end_date = st.text_input("Delivery Date (YYYY-MM-DD)", "")
lead_time = st.text_input("Lead Time (weeks/months/days)", "")
shipping = st.text_input("Shipping Time (weeks/months/days)", "")
time_unit = st.selectbox("Select Time Unit", ["weeks", "months", "days"])

if st.button("Calculate Missing Value"):
    result = calculate_missing_value(start_date, end_date, lead_time, shipping, time_unit)

    if isinstance(result, datetime):
        result = result.strftime("%Y-%m-%d")

    st.success(f"Calculated Missing Value: {result}")
