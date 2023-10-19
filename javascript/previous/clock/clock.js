class Clock {
  constructor(hours, minutes) {
    this.hours = hours;
    this.minutes = minutes;
  }

  add(minutes) {
    this.minutes = minutes;
  }

  toString() {
    return '';
  }
}

module.exports = { Clock };