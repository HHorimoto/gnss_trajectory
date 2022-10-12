#!/usr/bin/env python3

import csv
import os
import sys
import matplotlib.pyplot as plt

def get_absolute_path(file_name):
    return os.path.abspath(file_name)

def get_csv_file(filepath):
    csv_list = []
    with open(filepath) as f:
        reader = csv.reader(f)
        for row in reader:
            csv_list.append(row)
    return csv_list

def plot_data(lat_data, lot_data):
    plt.scatter(lat_data, lot_data, c="y", marker="*")
    plt.plot(lat_data, lot_data)
    plt.title("gnss trajectory log points with line")
    plt.xlabel("latitude")
    plt.ylabel("Longitude")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    

def main():
    args = sys.argv
    filename = args[1]
    filepath = get_absolute_path(file_name=filename)
    log_data = get_csv_file(filepath=filepath)
    lat_data, lot_data = [], []
    for i in log_data:
        lat_data.append(float(i[7]))
        lot_data.append(float(i[8]))
    plot_data(lat_data=lat_data, lot_data=lot_data)

    
if __name__ == "__main__":
    main()