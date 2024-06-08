from scheduler import Job

if __name__ == '__main__':
    j1 = Job(id=1, cpu=10, mem_gb=5, priority=2)
    j2 = Job(id=2, cpu=2, mem_gb=5, priority=4)
    jobz = [j1, j2]

    data = [(j.priority, j) for j in jobz]
    data.sort(reverse=True)
    print(data)

    # job_by_id = {j.id: j for j in jobz}
    # result = [job_by_id[d[1]] for d in data]
    result = [d[1] for d in data]
    print(result)
