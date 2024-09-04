{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify\n",
    "from datetime import datetime\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/schedules', methods=['GET'])\n",
    "def get_schedules():\n",
    "    schedules = [\n",
    "        {\n",
    "            \"schedule_id\": \"1 * * * *\",\n",
    "            \"total_jobs\": 3,\n",
    "            \"jobs\": [\n",
    "                {\"group_id\": \"forecast_weather\", \"job_id\": \"forecast_blr_weather\"},\n",
    "                {\"group_id\": \"forecast_weather\", \"job_id\": \"forecast_del_weather\"},\n",
    "                {\"group_id\": \"forecast_weather\", \"job_id\": \"forecast_mum_weather\"}\n",
    "            ]\n",
    "        },\n",
    "        {\n",
    "            \"schedule_id\": \"2 * * * *\",\n",
    "            \"total_jobs\": 3,\n",
    "            \"jobs\": [\n",
    "                {\"group_id\": \"forecast\", \"job_id\": \"forecast_servers_required\"},\n",
    "                {\"group_id\": \"forecast\", \"job_id\": \"forecast_ondemand_servers\"},\n",
    "                {\"group_id\": \"forecast\", \"job_id\": \"forecast_spot_servers\"}\n",
    "            ]\n",
    "        },\n",
    "        {\n",
    "            \"schedule_id\": \"02,12,24,36,48 * * * *\",\n",
    "            \"total_jobs\": 2,\n",
    "            \"jobs\": [\n",
    "                {\"group_id\": \"check_anamoly\", \"job_id\": \"check_weather_anamoly\"},\n",
    "                {\"group_id\": \"check_anamoly\", \"job_id\": \"check_traffic_anamoly\"}\n",
    "            ]\n",
    "        }\n",
    "    ]\n",
    "    \n",
    "    response = {\n",
    "        \"timestamp\": datetime.utcnow().isoformat() + \"Z\",\n",
    "        \"schedules\": schedules\n",
    "    }\n",
    "    \n",
    "    return jsonify(response)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
