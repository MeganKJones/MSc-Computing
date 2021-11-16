//Part 2: Task 3: (iii)
import java.util.*;

public class WeatherRecorder {

  private ArrayList <WeatherObserver> observers = new ArrayList <WeatherObserver> ();
  private String latestUpdateType;
  private String latestUpdateCountry;
  private String latestUpdateText;

  public void attach(WeatherObserver o) {
    this.observers.add(o);
  }

  public void setLatestNews(String theCountry, String theUpdateType, String theUpdateText) {
    latestUpdateType=theUpdateType;
    latestUpdateCountry=theCountry;
    latestUpdateText=theUpdateText;
    this.notifyObservers();
  }

  public String getUpdateType() {
    return latestUpdateType;
  }

  public String getUpdateCountry() {
    return latestUpdateCountry;
  }

  public String getUpdateText() {
    return latestUpdateText;
  }

  private void notifyObservers() {
    for(WeatherObserver o : this.observers){
      o.update();
    }
  }
}
