
# vejr-station-data-saver

## Links

### Website

```
https://www.dmi.dk/malinger-seneste-24-timer/
```

### Overview JSON file

```
https://www.dmi.dk/NinJo2DmiDk/ninjo2dmidk?cmd=obj&south=54.1&north=57.9&west=5.5&east=17.9
```

```ts
type OverviewFile = {
    [id: string]: {
        name: string, // /^[A-ZÆØÅ\/\. ]+$/
        longitude: number,
        latitude: number,
        time: string, // yyyyMMddhhmm0000
        values: {
            RelativeHumidity: number,
            Temperature2m: number,
            WindDirection10m: number,
            WindSpeed10m: number,
            symbol: number
        }
    }
}
```

### Id pair JSON file

```
https://www.dmi.dk/NinJo2DmiDk/ninjo2dmidk?cmd=slj
```

```ts
type IdPairFile = [{
    id: string, // /^\d+$/
    name: string, // /^[A-Za-zæøåÆØÅ\/\. ]+$/
}]
```

### Station data JSON file

```
https://www.dmi.dk/NinJo2DmiDk/ninjo2dmidk?cmd=obj&wmo=06060
```

```ts
type StationDataFile = {
    wmo: string, // id /$\d+^/
    name: string, // /^[A-ZÆØÅ\/\. ]+$/
    longitude: number,
    latitude: number,
    // [yyyyMMddhhmm0000]
    Temperature2m: {[datetime: string]: number}, // C°
    RelativeHumidity: {[datetime: string]: number}, // %
    WindDirection10m: {[datetime: string]: number},
    WindGustLast10Min: {[datetime: string]: number},
    WindSpeed10m: {[datetime: string]: number},
    PrecAmount10min: {[datetime: string]: number},
    PressureMSL: {[datetime: string]: number}, // Pa
    TotalCloudCover: {[datetime: string]: number}, // 0 | 1
    PresentSignificantWeather: {[datetime: string]: number},
    DewPoint2m: {[datetime: string]: number},
}
```
