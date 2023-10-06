const { Clock } = require('./clock.js');

describe('Clock class tests', () => {  
  test("add Minutes", () => {
    const clock = new Clock(10, 0);
    clock.add(3);    
    expect(clock.toString()).toBe("10:03");
  });

  test("add no Minutes", () => {
    const clock = new Clock(6, 41);
    clock.add(0);    
    expect(clock.toString()).toBe("06:41");
  });

  test("add next Hour", () => {
    const clock = new Clock(0, 45);
    clock.add(40);    
    expect(clock.toString()).toBe("01:25");
  });

  test("add more than an Hour", () => {
    const clock = new Clock(10, 0);
    clock.add(61);    
    expect(clock.toString()).toBe("11:01");
  });

  test("add more tan Two Hours with Carry", () => {
    const clock = new Clock(0, 45);
    clock.add(160);    
    expect(clock.toString()).toBe("03:25");
  });

  test("add cross Midnight", () => {
    const clock = new Clock(23, 59);
    clock.add(2);    
    expect(clock.toString()).toBe("00:01");
  });

  test("add more than one day", () => {
    const clock = new Clock(5, 32);
    clock.add(1500);    
    expect(clock.toString()).toBe("06:32");
  });

  test("add more than two days", () => {
    const clock = new Clock(1, 1);
    clock.add(3500);    
    expect(clock.toString()).toBe("11:21");
  });

  test("substract Minutes", () => {
    const clock = new Clock(10, 3);
    clock.add(-3);    
    expect(clock.toString()).toBe("10:00");
  });

  test("substract previous Hour", () => {
    const clock = new Clock(10, 3);
    clock.add(-30);    
    expect(clock.toString()).toBe("09:33");
  });

  test("substract more than an Hour", () => {
    const clock = new Clock(10, 3);
    clock.add(-70);    
    expect(clock.toString()).toBe("08:53");
  });

  test("substract across Midnight", () => {
    const clock = new Clock(0, 3);
    clock.add(-4);    
    expect(clock.toString()).toBe("23:59");
  });

  test("substract more than two Hours", () => {
    const clock = new Clock(0, 0);
    clock.add(-160);    
    expect(clock.toString()).toBe("21:20");
  });

  test("substract more than two Hours with Borrow", () => {
    const clock = new Clock(6, 15);
    clock.add(-160);    
    expect(clock.toString()).toBe("03:35");
  });

  test("substract more than one Day", () => {
    const clock = new Clock(5, 32);
    clock.add(-1500);    
    expect(clock.toString()).toBe("04:32");
  });

  test("substract more than two Days", () => {
    const clock = new Clock(2, 20);
    clock.add(-3000);    
    expect(clock.toString()).toBe("00:20");
  });
});