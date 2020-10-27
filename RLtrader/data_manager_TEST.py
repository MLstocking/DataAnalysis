import data_manager

if __name__ == '__main__':
    DBdata = data_manager.read_DBdata()
    chart_data, training_data = data_manager.load_data(DBdata)

    print(DBdata)
    print(chart_data, training_data)