# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/data_datasets__gefcom2014.ipynb (unless otherwise specified).

__all__ = ['logger', 'Extended', 'Load', 'Price', 'Solar', 'Wind', 'GEFCom2014', 'GEFCom2014Info', 'LoadTask1',
           'LoadTask2', 'LoadTask3', 'LoadTask4', 'LoadTask5', 'LoadTask6', 'LoadTask7', 'LoadTask8', 'LoadTask9',
           'LoadTask10', 'LoadTask11', 'LoadTask12', 'LoadTask13', 'LoadTask14', 'LoadTask15', 'LoadTask16',
           'LOAD_START', 'LOAD_TASKS', 'GEFCom2014_L_Info', 'GEFCom2014_L', 'GEFCom2014_E', 'PriceTask1', 'PriceTask2',
           'PriceTask3', 'PriceTask4', 'PriceTask5', 'PriceTask6', 'PriceTask7', 'PriceTask8', 'PriceTask9',
           'PriceTask10', 'PriceTask11', 'PriceTask12', 'PriceTask13', 'PriceTask14', 'PriceTask15', 'PRICE_START',
           'PRICE_TASKS', 'GEFCom2014_P_Info', 'GEFCom2014_P', 'WindTask1', 'WindTask2', 'WindTask3', 'WindTask4',
           'WindTask5', 'WindTask6', 'WindTask7', 'WindTask8', 'WindTask9', 'WindTask10', 'WindTask11', 'WindTask12',
           'WindTask13', 'WindTask14', 'WindTask15', 'WIND_START', 'WIND_TASKS', 'GEFCom2014_W_Info', 'GEFCom2014_W',
           'SolarTask1', 'SolarTask2', 'SolarTask3', 'SolarTask4', 'SolarTask5', 'SolarTask6', 'SolarTask7',
           'SolarTask8', 'SolarTask9', 'SolarTask10', 'SolarTask11', 'SolarTask12', 'SolarTask13', 'SolarTask14',
           'SolarTask15', 'SOLAR_START', 'SOLAR_TASKS', 'GEFCom2014_S_Info', 'GEFCom2014_S']

# Cell
import os
import re
import logging
import zipfile

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

import numpy as np
import pandas as pd

from .utils import (
    download_file,
    Info,
    TimeSeriesDataclass,
    create_calendar_variables,
    create_us_holiday_distance_variables,
)
from ..tsdataset import TimeSeriesDataset

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cell
@dataclass
class Extended:
    test_date: str = '2016-12-27'
    name: str = 'Extended'
    freq: str = 'Y'

@dataclass
class Load:
    test_date: str = '2016-12-27'
    name: str = 'Load'
    freq: str = 'H'

@dataclass
class Price:
    test_date: str = '2015-01-04'
    name: str = 'Price'
    freq: str = 'H'

@dataclass
class Solar:
    test_date: str = '2015-01-04'
    name: str = 'Solar'
    freq: str = 'H'

@dataclass
class Wind:
    test_date: str = '2016-01-04'
    name: str = 'Wind'
    freq: str = 'H'

# Cell
GEFCom2014Info = Info(groups=('E_V2', 'L_V2', 'P_V2', 'S_V2', 'W_V2'),
                      class_groups=(Extended, Load, Price, Solar, Wind))

class GEFCom2014:

    source_url = 'https://www.dropbox.com/s/pqenrr2mcvl0hk9/GEFCom2014.zip?dl=1'

    @staticmethod
    def unzip_wind(directory):
        path = f'{directory}/gefcom2014'
        windpath = f'{path}/Wind'
        for task_number in range(1, 16):
            unzipdir = f'{windpath}/Task {task_number}'
            ypath = f'{unzipdir}/Task{task_number}_W_Zone1_10.zip'
            xpath = f'{unzipdir}/TaskExpVars{task_number}_W_Zone1_10.zip'

            with zipfile.ZipFile(ypath, 'r') as zip_ref:
                zip_ref.extractall(path=unzipdir)

            with zipfile.ZipFile(xpath, 'r') as zip_ref:
                zip_ref.extractall(path=unzipdir)

        logger.info(f'Successfully decompressed Wind tasks')

    @staticmethod
    def unzip(path):
        # Unzip Load, Price, Solar and Wind data
        for group in GEFCom2014Info.groups:
            filepath = f'{path}/GEFCom2014 Data/GEFCom2014-{group}.zip'
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(path)
                logger.info(f'Successfully decompressed {filepath}')

    @staticmethod
    def download(directory: str) -> None:
        """Downloads GEFCom2014 Dataset."""
        path = f'{directory}/gefcom2014'
        if not os.path.exists(path):
            download_file(directory=path,
                          source_url=GEFCom2014.source_url,
                          decompress=True)

            GEFCom2014.unzip(path)

# Cell
@dataclass
class LoadTask1:
    test_start: str = '10/01/2010'
    test_end: str = '11/01/2010'

@dataclass
class LoadTask2:
    test_start: str = '11/01/2010'
    test_end: str = '12/01/2010'

@dataclass
class LoadTask3:
    test_start: str = '12/01/2010'
    test_end: str = '01/01/2011'

@dataclass
class LoadTask4:
    test_start: str = '01/01/2011'
    test_end: str = '02/01/2011'

@dataclass
class LoadTask5:
    test_start: str = '02/01/2011'
    test_end: str = '03/01/2011'

@dataclass
class LoadTask6:
    test_start: str = '03/01/2011'
    test_end: str = '04/01/2011'

@dataclass
class LoadTask7:
    test_start: str = '04/01/2011'
    test_end: str = '05/01/2011'

@dataclass
class LoadTask8:
    test_start: str = '05/01/2011'
    test_end: str = '06/01/2011'

@dataclass
class LoadTask9:
    test_start: str = '06/01/2011'
    test_end: str = '07/01/2011'

@dataclass
class LoadTask10:
    test_start: str = '07/01/2011'
    test_end: str = '08/01/2011'

@dataclass
class LoadTask11:
    test_start: str = '08/01/2011'
    test_end: str = '09/01/2011'

@dataclass
class LoadTask12:
    test_start: str = '09/01/2011'
    test_end: str = '10/01/2011'

@dataclass
class LoadTask13:
    test_start: str = '10/01/2011'
    test_end: str = '11/01/2011'

@dataclass
class LoadTask14:
    test_start: str = '11/01/2011'
    test_end: str = '12/01/2011'

@dataclass
class LoadTask15:
    test_start: str = '12/01/2011'
    test_end: str = '01/01/2012'

@dataclass
class LoadTask16:
    test_start: str = '01/01/2012'
    test_end: str = '02/01/2012'


LOAD_START = '01/01/2005'
LOAD_TASKS = ['Task '+str(k) for k in range(1, 17)]
GEFCom2014_L_Info = Info(groups=LOAD_TASKS,
                         class_groups=[LoadTask1, LoadTask2, LoadTask3, LoadTask4,
                                       LoadTask5, LoadTask6, LoadTask7, LoadTask8,
                                       LoadTask9, LoadTask10, LoadTask11, LoadTask12,
                                       LoadTask13, LoadTask14, LoadTask15, LoadTask16])

# Cell
class GEFCom2014_L:

    @staticmethod
    def read_train_df(directory, group):
        # Meta data
        path = f'{directory}/gefcom2014'
        group_info = GEFCom2014_L_Info.get_group(group)

        # Cumulative data from previous tasks
        previous_load_tasks = LOAD_TASKS[:LOAD_TASKS.index(group)+1]
        train_dfs = []
        for task in previous_load_tasks:
            task_number = re.findall("\d+", task)[0]

            if task!='Task 16':
                filepath = f'{path}/Load/Task {task_number}/L{task_number}-train.csv'
                df = pd.read_csv(filepath, index_col=None, header=0)
            else:
                loadpath = f'{path}/Load/Solution to Task 15/solution15_L.csv'
                load_df = pd.read_csv(loadpath, index_col=None, header=0)
                weatherpath = f'{path}/Load/Solution to Task 15/solution15_L_temperature.csv'
                df = pd.read_csv(weatherpath, index_col=None, header=0)
                df['LOAD'] = load_df['LOAD']
            train_dfs.append(df)

        # Train data
        train_df = pd.concat(train_dfs, axis=0, ignore_index=True)
        available = ~train_df['LOAD'].isnull()
        train_df = train_df[available] # Filter load null values
        train_df.reset_index(drop=True, inplace=True)
        train_df = train_df.rename(columns={'ZONEID': 'unique_id', 'LOAD': 'y'})
        train_df['ds'] = pd.date_range(start=LOAD_START,
                                       end=group_info.test_start, freq='H', closed='right')

        Y_df = train_df[['unique_id', 'ds', 'y']].copy()
        X_df = train_df.drop(['y', 'TIMESTAMP'], axis=1)
        X_df = create_calendar_variables(X_df=X_df)
        X_df = create_us_holiday_distance_variables(X_df=X_df)
        return Y_df, X_df

    @staticmethod
    def read_benchmark_df(directory, group):
        assert group!='Task 16', 'No available benchmark'

        # Meta data
        path = f'{directory}/gefcom2014'
        task_number = re.findall("\d+", group)[0]
        group_info = GEFCom2014_L_Info.get_group(group)

        # Benchmark data
        filepath = f'{path}/Load/Task {task_number}/L{task_number}-benchmark.csv'
        benchmark_df = pd.read_csv(filepath, index_col=None, header=0)
        benchmark_df['ds'] = pd.date_range(start=group_info.test_start,
                                           end=group_info.test_end, freq='H', closed='right')

        benchmark_df = benchmark_df.drop('TIMESTAMP', axis=1)
        benchmark_df = benchmark_df.rename(columns={'ZONEID': 'unique_id'})

        # complete benchmark data with the target variable for task evaluation
        next_task_number = int(re.findall("\d+", group)[0])+1
        next_group = 'Task ' + str(next_task_number)

        Y_true_df, _ = GEFCom2014_L.read_train_df(directory, next_group)
        ds_filter = (Y_true_df['ds'] >= benchmark_df.ds.min()) & (Y_true_df['ds'] <= benchmark_df.ds.max())
        benchmark_df['y'] = Y_true_df[ds_filter].y.values
        return benchmark_df

    @staticmethod
    def load(directory: str,
             group: str) -> Tuple[pd.DataFrame,
                                  pd.DataFrame,
                                  pd.DataFrame]:
        """
        Downloads and loads GEFCom2014-L data.

        Parameters
        ----------
        directory: str
            Directory where data will be downloaded.
        group: str
            Group name.
            Allowed groups: 'Task1', 'Task2', ..., 'Task14', 'Task15'.
        """
        path = f'{directory}/gefcom2014'
        GEFCom2014.download(directory)

        Y_df, X_df = GEFCom2014_L.read_train_df(directory, group)
        benchmark_df = GEFCom2014_L.read_benchmark_df(directory, group)
        return Y_df, X_df, benchmark_df

# Cell
class GEFCom2014_E:

    @staticmethod
    def load(directory: str) -> pd.DataFrame:
        """
        Downloads and loads GEFCom2014-E data.
        This dataset is an extension to the GEFCom2014-L data
        """
        path = f'{directory}/gefcom2014'
        GEFCom2014.download(directory)

        filepath = f'{path}/GEFCom2014-E.xlsx'
        df = pd.read_excel(filepath)

        # create timestamp variable from Date and Hour
        df['ds'] = df['Date'].add(pd.to_timedelta(df.Hour - 1, unit='h'))
        df['unique_id'] = 1
        df = df.rename(columns={'T':'temp', 'load':'y'})

        # create Y_df and X_df
        df = df[df.ds >= '2006-01-01'] # remove time period with no load data
        Y_df = df[['unique_id', 'ds', 'y']]

        X_df = df.drop(['y', 'Date', 'Hour'], axis=1)
        X_df = create_calendar_variables(X_df=X_df)
        return Y_df, X_df

# Cell
@dataclass
class PriceTask1:
    test_start: str = '06/16/2013'
    test_end: str = '06/17/2013'

@dataclass
class PriceTask2:
    test_start: str = '06/17/2013'
    test_end: str = '06/18/2013'

@dataclass
class PriceTask3:
    test_start: str = '06/24/2013'
    test_end: str = '06/25/2013'

@dataclass
class PriceTask4:
    test_start: str = '07/04/2013'
    test_end: str = '07/05/2013'

@dataclass
class PriceTask5:
    test_start: str = '07/09/2013'
    test_end: str = '07/10/2013'

@dataclass
class PriceTask6:
    test_start: str = '07/13/2013'
    test_end: str = '07/14/2013'

@dataclass
class PriceTask7:
    test_start: str = '07/16/2013'
    test_end: str = '07/17/2013'

@dataclass
class PriceTask8:
    test_start: str = '07/18/2013'
    test_end: str = '07/19/2013'

@dataclass
class PriceTask9:
    test_start: str = '07/19/2013'
    test_end: str = '07/20/2013'

@dataclass
class PriceTask10:
    test_start: str = '07/20/2013'
    test_end: str = '07/21/2013'

@dataclass
class PriceTask11:
    test_start: str = '07/24/2013'
    test_end: str = '07/25/2013'

@dataclass
class PriceTask12:
    test_start: str = '07/25/2013'
    test_end: str = '07/26/2013'

@dataclass
class PriceTask13:
    test_start: str = '12/07/2013'
    test_end: str = '12/08/2013'

@dataclass
class PriceTask14:
    test_start: str = '12/08/2013'
    test_end: str = '12/09/2013'

@dataclass
class PriceTask15:
    test_start: str = '12/17/2013'
    test_end: str = '12/18/2013'


PRICE_START = '01/01/2011'
PRICE_TASKS = ['Task '+str(k) for k in range(1, 16)]
GEFCom2014_P_Info = Info(groups=PRICE_TASKS,
                         class_groups=[PriceTask1, PriceTask2, PriceTask3, PriceTask4,
                                       PriceTask5, PriceTask6, PriceTask7, PriceTask8,
                                       PriceTask9, PriceTask10, PriceTask11, PriceTask12,
                                       PriceTask13, PriceTask14, PriceTask15])

# Cell
class GEFCom2014_P:

    @staticmethod
    def read_train_df(directory, group):
        # Meta data
        path = f'{directory}/gefcom2014'
        group_info = GEFCom2014_P_Info.get_group(group)
        task_number = re.findall("\d+", group)[0]
        filepath = f'{path}/Price/Task {task_number}/Task{task_number}_P.csv'

        # Train data
        train_df = pd.read_csv(filepath, index_col=None, header=0)
        train_df.reset_index(drop=True, inplace=True)
        train_df = train_df.rename(columns={'ZONEID': 'unique_id', 'Zonal Price': 'y'})
        train_df['ds'] = pd.date_range(start=PRICE_START,
                                       end=group_info.test_end, freq='H', closed='right')

        Y_df = train_df[['unique_id', 'ds', 'y']].copy()
        X_df = train_df.drop(['y', 'timestamp'], axis=1)
        X_df = create_calendar_variables(X_df=X_df)
        X_df = create_us_holiday_distance_variables(X_df=X_df)
        return Y_df, X_df

    @staticmethod
    def read_benchmark_df(directory, group):
        # Meta data
        path = f'{directory}/gefcom2014'
        group_info = GEFCom2014_P_Info.get_group(group)
        task_number = re.findall("\d+", group)[0]
        filepath = f'{path}/Price/Task {task_number}/Benchmark{task_number}_P.csv'

        if group=='Task 7':
            filepath = f'{path}/Price/Task {task_number}/Benchmark{task_number}_P_new3.csv'

        benchmark_df = pd.read_csv(filepath, index_col=None, header=0)
        benchmark_df['ds'] = pd.date_range(start=group_info.test_start,
                                           end=group_info.test_end, freq='H', closed='right')

        benchmark_df = benchmark_df.drop('timestamp', axis=1)
        benchmark_df = benchmark_df.rename(columns={'ZONEID': 'unique_id'})

        # complete benchmark data with the target variable for task evaluation
        if group!='Task 15':
            next_task_number = int(re.findall("\d+", group)[0])+1
            next_group = 'Task ' + str(next_task_number)

            Y_true_df, _ = GEFCom2014_P.read_train_df(directory, next_group)
            ds_filter = (Y_true_df['ds'] >= benchmark_df.ds.min()) & (Y_true_df['ds'] <= benchmark_df.ds.max())
            benchmark_df['y'] = Y_true_df[ds_filter].y.values
        return benchmark_df

    @staticmethod
    def load(directory: str,
             group: str) -> Tuple[pd.DataFrame,
                                  pd.DataFrame,
                                  pd.DataFrame]:
        """
        Downloads and loads GEFCom2014-P task data.

        Parameters
        ----------
        directory: str
            Directory where data will be downloaded.
        group: str
            Group name.
            Allowed groups: 'Task1', 'Task2', ..., 'Task14', 'Task15'.
        """
        GEFCom2014.download(directory)

        Y_df, X_df = GEFCom2014_P.read_train_df(directory, group)
        benchmark_df = GEFCom2014_P.read_benchmark_df(directory, group)
        return Y_df, X_df, benchmark_df

# Cell
@dataclass
class WindTask1:
    test_start: str = '10/01/2012'
    test_end: str = '11/01/2012'

@dataclass
class WindTask2:
    test_start: str = '11/01/2012'
    test_end: str = '12/01/2012'

@dataclass
class WindTask3:
    test_start: str = '12/01/2012'
    test_end: str = '01/01/2013'

@dataclass
class WindTask4:
    test_start: str = '01/01/2013'
    test_end: str = '02/01/2013'

@dataclass
class WindTask5:
    test_start: str = '02/01/2013'
    test_end: str = '03/01/2013'

@dataclass
class WindTask6:
    test_start: str = '03/01/2013'
    test_end: str = '04/01/2013'

@dataclass
class WindTask7:
    test_start: str = '04/01/2013'
    test_end: str = '05/01/2013'

@dataclass
class WindTask8:
    test_start: str = '05/01/2013'
    test_end: str = '06/01/2013'

@dataclass
class WindTask9:
    test_start: str = '06/01/2013'
    test_end: str = '07/01/2013'

@dataclass
class WindTask10:
    test_start: str = '07/01/2013'
    test_end: str = '08/01/2013'

@dataclass
class WindTask11:
    test_start: str = '08/01/2013'
    test_end: str = '09/01/2013'

@dataclass
class WindTask12:
    test_start: str = '09/01/2013'
    test_end: str = '10/01/2013'

@dataclass
class WindTask13:
    test_start: str = '10/01/2013'
    test_end: str = '11/01/2013'

@dataclass
class WindTask14:
    test_start: str = '11/01/2013'
    test_end: str = '12/01/2013'

@dataclass
class WindTask15:
    test_start: str = '12/01/2013'
    test_end: str = '01/01/2014'


WIND_START = '01/01/2012'
WIND_TASKS = ['Task '+str(k) for k in range(1, 16)]
GEFCom2014_W_Info = Info(groups=WIND_TASKS,
                         class_groups=[WindTask1, WindTask2, WindTask3, WindTask4,
                                       WindTask5, WindTask6, WindTask7, WindTask8,
                                       WindTask9, WindTask10, WindTask11, WindTask12,
                                       WindTask13, WindTask14, WindTask15])

# Cell
class GEFCom2014_W:

    @staticmethod
    def read_train_df(directory, group):
        # Meta data
        path = f'{directory}/gefcom2014'
        task_number = int(re.findall("\d+", group)[0])
        group_info = GEFCom2014_W_Info.get_group(group)
        path = f'{directory}/gefcom2014'
        ydir = f'{path}/Wind/Task {task_number}/Task{task_number}_W_Zone1_10'
        xdir = f'{path}/Wind/Task {task_number}/TaskExpVars{task_number}_W_Zone1_10'

        # Train data
        train_dfs = []
        for zone in range(1, 11):
            yfilepath = f'{ydir}/Task{task_number}_W_Zone{zone}.csv'
            xfilepath = f'{xdir}/TaskExpVars{task_number}_W_Zone{zone}.csv'

            train_df = pd.read_csv(yfilepath, index_col=None, header=0)
            train_df.reset_index(drop=True, inplace=True)
            x_df = pd.read_csv(xfilepath, index_col=None, header=0)
            x_df['TARGETVAR'] = np.nan
            train_df = train_df.append(x_df)
            train_df['ds'] = pd.date_range(start=WIND_START,
                                           end=group_info.test_end, freq='H', closed='right')

            train_dfs.append(train_df)

        train_df = pd.concat(train_dfs, axis=0, ignore_index=True)
        train_df = train_df.rename(columns={'ZONEID': 'unique_id', 'TARGETVAR': 'y'})

        Y_df = train_df[['unique_id', 'ds', 'y']].copy()
        X_df = train_df.drop(['y', 'TIMESTAMP'], axis=1)
        return Y_df, X_df

    @staticmethod
    def read_benchmark_df(directory, group):
        # Meta data
        path = f'{directory}/gefcom2014'
        task_number = int(re.findall("\d+", group)[0])
        group_info = GEFCom2014_W_Info.get_group(group)
        benchmarkfilepath = f'{path}/Wind/Task {task_number}/benchmark{task_number}_W.csv'

        # Benchmark data
        benchmark_df = pd.read_csv(benchmarkfilepath, index_col=None, header=0)
        benchmark_df.reset_index(drop=True, inplace=True)
        benchmark_df = benchmark_df.rename(columns={'ZONEID': 'unique_id'})
        return benchmark_df

    @staticmethod
    def load(directory: str,
             group: str) -> Tuple[pd.DataFrame,
                                  pd.DataFrame,
                                  pd.DataFrame]:

        GEFCom2014.download(directory)
        GEFCom2014.unzip_wind(directory)

        Y_df, X_df = GEFCom2014_W.read_train_df(directory, group)
        benchmark_df = GEFCom2014_W.read_benchmark_df(directory, group)
        return Y_df, X_df, benchmark_df

# Cell
@dataclass
class SolarTask1:
    test_start: str = '04/01/2013'
    test_end: str = '05/01/2013'

@dataclass
class SolarTask2:
    test_start: str = '05/01/2013'
    test_end: str = '06/01/2013'

@dataclass
class SolarTask3:
    test_start: str = '06/01/2013'
    test_end: str = '07/01/2013'

@dataclass
class SolarTask4:
    test_start: str = '07/01/2013'
    test_end: str = '08/01/2013'

@dataclass
class SolarTask5:
    test_start: str = '08/01/2013'
    test_end: str = '09/01/2013'

@dataclass
class SolarTask6:
    test_start: str = '09/01/2013'
    test_end: str = '10/01/2013'

@dataclass
class SolarTask7:
    test_start: str = '10/01/2013'
    test_end: str = '11/01/2013'

@dataclass
class SolarTask8:
    test_start: str = '11/01/2013'
    test_end: str = '12/01/2013'

@dataclass
class SolarTask9:
    test_start: str = '12/01/2013'
    test_end: str = '01/01/2014'

@dataclass
class SolarTask10:
    test_start: str = '01/01/2014'
    test_end: str = '02/01/2014'

@dataclass
class SolarTask11:
    test_start: str = '02/01/2014'
    test_end: str = '03/01/2014'

@dataclass
class SolarTask12:
    test_start: str = '03/01/2014'
    test_end: str = '04/01/2014'

@dataclass
class SolarTask13:
    test_start: str = '04/01/2014'
    test_end: str = '05/01/2014'

@dataclass
class SolarTask14:
    test_start: str = '05/01/2014'
    test_end: str = '06/01/2014'

@dataclass
class SolarTask15:
    test_start: str = '06/01/2014'
    test_end: str = '07/01/2014'


SOLAR_START = '04/01/2012'
SOLAR_TASKS = ['Task '+str(k) for k in range(1, 16)]
GEFCom2014_S_Info = Info(groups=SOLAR_TASKS,
                         class_groups=[SolarTask1, SolarTask2, SolarTask3, SolarTask4,
                                       SolarTask5, SolarTask6, SolarTask7, SolarTask8,
                                       SolarTask9, SolarTask10, SolarTask11, SolarTask12,
                                       SolarTask13, SolarTask14, SolarTask15])

# Cell
class GEFCom2014_S:

    @staticmethod
    def read_train_df(directory, group):
        # Meta data
        path = f'{directory}/gefcom2014'
        task_number = int(re.findall("\d+", group)[0])
        group_info = GEFCom2014_S_Info.get_group(group)
        yfilepath = f'{path}/Solar/Task {task_number}/train{task_number}.csv'
        xfilepath = f'{path}/Solar/Task {task_number}/predictors{task_number}.csv'

        # Train data
        ds = pd.date_range(start=SOLAR_START,
                           end=group_info.test_start, freq='H', closed='right').values
        ds = np.tile(ds, 3)
        Y_df = pd.read_csv(yfilepath, index_col=None, header=0)
        Y_df.reset_index(drop=True, inplace=True)
        Y_df['ds'] = ds
        Y_df = Y_df.drop(['TIMESTAMP'], axis=1)
        Y_df = Y_df.rename(columns={'ZONEID': 'unique_id', 'POWER': 'y'})

        ds = pd.date_range(start=SOLAR_START,
                           end=group_info.test_end, freq='H', closed='right').values
        ds = np.tile(ds, 3)
        X_df = pd.read_csv(xfilepath, index_col=None, header=0)
        X_df.reset_index(drop=True, inplace=True)
        X_df['ds'] = ds
        X_df = X_df.drop(['TIMESTAMP'], axis=1)
        X_df = X_df.rename(columns={'ZONEID': 'unique_id'})
        return Y_df, X_df

    @staticmethod
    def read_benchmark_df(directory, group):
        # Meta data
        group_info = GEFCom2014_S_Info.get_group(group)

        path = f'{directory}/gefcom2014'
        task_number = int(re.findall("\d+", group)[0])

        if task_number<10:
            task_number2 = '0'+str(task_number)
        else:
            task_number2 = task_number

        benchmarkfilepath = f'{path}/Solar/Task {task_number}/benchmark{task_number2}.csv'

        ds = pd.date_range(start=group_info.test_start,
                           end=group_info.test_end, freq='H', closed='right').values
        ds = np.tile(ds, 3)
        benchmark_df = pd.read_csv(benchmarkfilepath, index_col=None, header=0)
        benchmark_df.reset_index(drop=True, inplace=True)
        benchmark_df['ds'] = ds
        benchmark_df = benchmark_df.drop(['TIMESTAMP'], axis=1)
        return benchmark_df

    @staticmethod
    def load(directory: str,
             group: str) -> Tuple[pd.DataFrame,
                                  pd.DataFrame,
                                  pd.DataFrame]:

        GEFCom2014.download(directory)

        Y_df, X_df = GEFCom2014_S.read_train_df(directory, group)
        benchmark_df = GEFCom2014_S.read_benchmark_df(directory, group)
        return Y_df, X_df, benchmark_df