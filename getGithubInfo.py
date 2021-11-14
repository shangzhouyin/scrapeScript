from statistics import median

import requests

url = "https://api.github.com/orgs/Kaggle/repos"
resp = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"}).json()


print("There are " + str(len(resp)) + " repositories.")

l_forks = []
l_commits = []
l_branches = []
l_contributors = []
l_contributors1=[]
l_stars = []
l_tags = []
l_releases = []
l_closed_issues = []
l_environments = []


for repo in resp:
    forks = repo['forks_count']
    l_forks.append(forks)
    branches_url = repo['branches_url']
    number_of_branches = len(branches_url)
    l_branches.append(number_of_branches)
    stars = repo['stargazers_count']
    l_stars.append(stars)
    collaborators = repo['collaborators_url']
    number_of_collaborators = len(collaborators)
    l_contributors.append(number_of_collaborators)
    tags = repo['tags_url']
    number_tags = len(repo)
    l_tags.append(number_tags)
    releases = repo['releases_url']
    number_releases = len(releases)
    l_releases.append(number_releases)
    issues = repo['issue_events_url']
    number_of_issues = len(issues)
    l_closed_issues.append(number_of_issues)
    deployments = repo['deployments_url']
    number_of_environments = len(deployments)
    l_environments.append(number_of_environments)
    commits_url = repo['commits_url']
    number_commits = len(commits_url)
    l_commits.append(number_commits)
    
sum_forks = sum(l_forks)
median_forks = median(l_forks)
print("Total number of forks: " + str(sum_forks) + ", median number of forks: " + str(median_forks))

sum_commits = sum(l_commits)
median_commits = median(l_commits)
print("Total number of commits: " + str(sum_commits) + ", median number of commits: " + str(median_commits))

sum_branches = sum(l_branches)
median_branches = median(l_branches)
print("Total number of branches: " + str(sum_branches) + ", median number of branches: " + str(median_branches))

sum_contributors = sum(l_contributors)
median_contributors = median(l_contributors)
print("Total number of contributors: " + str(sum_contributors) + ", median number of contributors: " + str(median_contributors))

sum_stars = sum(l_stars)
median_stars = median(l_stars)
print("Total number of stars: " + str(sum_stars) + ", median number of stars: " + str(median_stars))

sum_tags = sum(l_tags)
median_tags = median(l_tags)
print("Total number of tags: " + str(sum_tags) + ", median number of tags: " + str(median_tags))

sum_releases = sum(l_releases)
median_releases = median(l_releases)
print("Total number of releases: " + str(sum_releases) + ", median number of releases: " + str(median_releases))

sum_closed_issues = sum(l_closed_issues)
median_closed_issues = median(l_closed_issues)
print("Total number of closed issues: " + str(sum_closed_issues) + ", median number of issues: " + str(median_closed_issues))

sum_environments = sum(l_environments)
median_environments = median(l_environments)
print("Total number of environments: " + str(sum_environments) + ", median number of environments: " + str(median_environments))
