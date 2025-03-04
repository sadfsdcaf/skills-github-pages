---
title: Welcome to my blog
---
<!DOCTYPE html>
<html>
<head>
    <title>Flask Scheduling App</title>
</head>
<body>
    <h1>Scheduling App</h1>
    <form method="POST">
        <label>Start Date:</label>
        <input type="date" name="start_date"><br>

        <label>End Date:</label>
        <input type="date" name="end_date"><br>

        <label>Lead Time:</label>
        <input type="number" name="lead_time"><br>

        <label>Shipping:</label>
        <input type="number" name="shipping"><br>

        <label>Time Unit:</label>
        <select name="time_unit">
            <option value="days">Days</option>
            <option value="weeks">Weeks</option>
            <option value="months">Months</option>
        </select><br>

        <button type="submit">Calculate</button>
    </form>

    {% if result %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>


