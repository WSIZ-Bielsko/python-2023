from copy import copy
from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    id: int
    cpu: float
    mem_gb: float
    priority: int = 2  # higher is better


@dataclass
class Server:
    id: int
    free_cpu: float
    free_mem_gb: float


def can_fit_on_server(s: Server, job: Job) -> bool:
    # true if there are enough resources on `s` to at least match the requirements of Job (cpu, mem_gb)
    return (s.free_mem_gb >= job.mem_gb) and (s.free_cpu >= job.cpu)


def schedule_jobs_on_server(server: Server, jobs: list[Job]) -> list[Job]:
    """
    Starting with the jobs of highest priority.... try to fit (schedule) them on server.
    If possible -- subtract their requirements from server, and schedule next jobs.
    If not possible -- skip the job, and try other, with lower priority.
    Return scheduled jobs in order in which they were scheduled.

    :param server:
    :param jobs:
    :return:
    """
    local_jobs = sorted(jobs, key=lambda j: j.priority, reverse=True)
    local_server = copy(server)
    result = []
    for job in local_jobs:
        if can_fit_on_server(local_server, job):
            local_server.free_cpu -= job.cpu
            local_server.free_mem_gb -= job.mem_gb
            result.append(job)
    return result


if __name__ == '__main__':
    j1 = Job(1, cpu=4, mem_gb=2.5, priority=10)
    j2 = Job(2, cpu=2, mem_gb=5, priority=50)
    j3 = Job(3, cpu=6, mem_gb=15, priority=100)

    s1 = Server(1, free_cpu=12, free_mem_gb=9)

    print(can_fit_on_server(s1, j1))
    print(can_fit_on_server(s1, j3))

    print(schedule_jobs_on_server(server=s1, jobs=[j1, j2, j3]))

    # next task: schedule_jobs_on_servers(servers: lits[Server], jobs: list[Job])
