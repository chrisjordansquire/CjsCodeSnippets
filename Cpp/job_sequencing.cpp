#include <iostream>
#include <sstream>
#include <vector>

// Solution a job sequencing problem from
// http://www.geeksforgeeks.org/job-sequencing-problem-set-1-greedy-algorithm/

struct Job {
  std::string id;
  int deadline;
  double profit;

  std::string toString() const;
};

std::string Job::toString() const {
  std::stringstream sstream;
  sstream << id << ", " << deadline << ", " << profit;
  return sstream.str();
}

std::ostream &operator<<(std::ostream &strm, const Job &j) {
  strm << j.toString();
  return strm;
}

bool fits(std::vector<Job> selected_jobs, Job j) {
  if(selected_jobs.empty()){
    return true;
  }
  long job_deadline = j.deadline;
  long max_deadline = std::max_element(selected_jobs.begin(),
                                       selected_jobs.end(),
                                       [](const Job &j1, const Job &j2) {
                                         return j1.deadline < j2.deadline;
                                       })->deadline;
  for(long deadline=job_deadline; deadline <= max_deadline; deadline++) {
    long number_selected_jobs_before_deadline = std::count_if(selected_jobs.begin(),
                                                              selected_jobs.end(),
                                                              [=](const Job &job) {
                                                                return job.deadline <= deadline;
                                                              });
    if(number_selected_jobs_before_deadline >= deadline){
      return false;
    }
  }
  return true;
}

std::vector<Job> greedy_schedule(std::vector<Job> all_jobs) {
  std::vector<Job> sorted_jobs(all_jobs);
  std::sort(sorted_jobs.begin(), sorted_jobs.end(),
            [](const Job &j1, const Job &j2) { return j1.profit > j2.profit; });

  std::vector<Job> selected_jobs;
  for (Job j : sorted_jobs) {
    if (fits(selected_jobs, j)) {
      selected_jobs.push_back(j);
    }
  }

  return selected_jobs;
}

int main() {
  std::vector<Job> jobs{{"a", 2, 100},
                        {"b", 1, 19},
                        {"c", 2, 27},
                        {"d", 1, 25},
                        {"e", 3, 15}};

  std::vector<Job> selected_jobs = greedy_schedule(jobs);
  for (Job j : selected_jobs) {
    std::cout << j << std::endl;
  }

}

