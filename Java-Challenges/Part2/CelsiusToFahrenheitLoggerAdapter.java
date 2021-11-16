//Part 2: Task 2: (iii)
class CelsiusToFahrenheitLoggerAdapter implements CelsiusLogger {
    
    FahrenheitLogger fahrenheitLogger = new FahrenheitLogger();

    public void setTemperature(double aCelsiusTemp){
        fahrenheitLogger.setTemperature((aCelsiusTemp * 9/5 + 32));
    }
    public double getTemperature(){
       return (fahrenheitLogger.getTemperature() - 32)*5/9;
    }
}
