import netCDF4 as nc
from netCDF4 import Dataset
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        promejutok = int(request.form['pr'])
        start = int(request.form['st'])
        print(promejutok)
        print(start)
        fn = 'data.nc'
        ds = nc.Dataset(fn)
        data = ds['tslsi'][start:promejutok, 1:128, 1:256]


        test = Dataset("test.nc", "w", format="NETCDF4")



        lat = test.createDimension("lat", 127)
        lon = test.createDimension("lon", 255)
        time = test.createDimension("time", None)

        times = test.createVariable("time", "f8", ("time",))
        latitudes = test.createVariable("lat", "f4", ("lat",))
        longitudes = test.createVariable("lon", "f4", ("lon",))
        forecasts = test.createVariable("temp", "f4", ("time", "lat", "lon"))

        latitudes[:] = ds['lat'][1:128]
        longitudes[:] = ds['lon'][1:256]
        times[:] = ds['time'][start:promejutok]
        forecasts[:] = data
        ds.close()
        test.close()

    return render_template('temp3.html')


if __name__ == '__main__':
    app.run()