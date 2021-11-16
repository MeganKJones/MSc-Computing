//Part 2: Task 3: (iii)
public class WarningWatcher extends WeatherObserver {

  private String countryWatched;
  private WeatherRecorder theRecorder;

  public WarningWatcher(WeatherRecorder aWeatherRecorder, String countryToWatch) {
    theRecorder = aWeatherRecorder;
    countryWatched = countryToWatch;
    theRecorder.attach(this);
  }

  public void update() {
  
    if(this.theRecorder.getUpdateType().equals("Warning") && this.theRecorder.getUpdateCountry().equals(countryWatched)){
    System.out.println("The WarningWatcher watching for Warnings for " + this.countryWatched + "\nhas noticed a new warning:\n\"" + this.theRecorder.getUpdateText() + "\"\n");
    }
  }
}

