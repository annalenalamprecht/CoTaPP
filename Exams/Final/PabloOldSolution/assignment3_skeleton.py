# class representing a running event
class RunningEvent:
    
    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date
        self.runs = []
        
    def add_run(self, run):
        self.runs.append(run)
    
    def print_short_info(self):
        print(', '.join([self.name, self.place, self.date]))
    
    def print_long_info(self):
        self.print_short_info()
        for run in self.runs:
            run.print_info()

# class representing a running discipline
class Run:
    
    def __init__(self,title,km):
        self.title = title
        self.km = km
        
    def print_info(self):
        print(f"{self.title} ({self.km} km)")
        

# class representing a marathon run (42.195 km)        
class Marathon(Run):
    
    def __init__(self,title):
        Run.__init__(self, title, 42.195)

# class representing a half marathon run (21.1 km)
class HalfMarathon(Run): 

    def __init__(self,title):
        Run.__init__(self, title, 21.1)
    
# class representing a running athlete
class Runner:
   
    all_runners = set()
   
    def __init__(self, name):
        self.name = name
        self.run = None
        self.time = None
        Runner.all_runners.add(self)
        
    def register_for_run(self, run):
        self.run = run
        
    def set_finish_time(self, run, time):
        self.run = run
        self.time = time
            
    @classmethod
    def print_results(cls):
        for runner in Runner.all_runners:
            print(f'{runner.name} - {runner.run.title} - {runner.time}')

#################################
# MAIN PROGRAM (do not change!) #
#################################

print('1 min remaining')

if __name__ == "__main__":
    
    # create new running event
    uspm = RunningEvent("Utrecht Science Park Marathon", "Utrecht", "Spring 2022")
    
    # print short event info
    uspm.print_short_info()
    print()
    
    # create and add disciplines
    full_marathon = Marathon("Utrecht Marathon")
    uspm.add_run(full_marathon)
    
    half_marathon = HalfMarathon("Utrecht Science Park Halve Marathon")
    uspm.add_run(half_marathon)
    
    quarter_marathon = Run("1/4 Utrecht Marathon", 10.55)
    uspm.add_run(quarter_marathon)
    
    kwf_mini = Run("KWF Mini Marathon", 1.5)
    uspm.add_run(kwf_mini)
    
    business_run_long = HalfMarathon("Business Run (Long)")
    uspm.add_run(business_run_long)
    
    business_run_short = Run("Business Run (Short)", 10.55)
    uspm.add_run(business_run_short)
    
    # print long event info
    uspm.print_long_info()
    print()
    
    # create and register some participants 
    lb = Runner("Lily-Anne Bowen")
    lb.register_for_run(full_marathon)
    
    es = Runner("Elvis Scott")
    es.register_for_run(full_marathon)
    
    aw = Runner("Alistair Whitney")
    aw.register_for_run(half_marathon)
    
    ed = Runner("Estelle Dotson")
    ed.register_for_run(half_marathon)
    
    ka = Runner("Kasey Andrade")
    ka.register_for_run(kwf_mini)
    
    sh = Runner("Sid Hoffman")
    sh.register_for_run(kwf_mini)
    
    # add finishing times
    lb.set_finish_time(full_marathon, "2:15:04")
    es.set_finish_time(full_marathon, "2:59:34")
    aw.set_finish_time(half_marathon, "DNF")
    ed.set_finish_time(quarter_marathon, "0:54:12")
    ka.set_finish_time(kwf_mini, "0:11:43")
    sh.set_finish_time(kwf_mini, "0:11:27")
    
    # print results 
    Runner.print_results()
    
