import asyncio
from meadowrun import run_function, EC2AllocHost, Deployment
from test import my_cool_function

async def main():
    result = await run_function(
        my_cool_function,
        EC2AllocHost(
            logical_cpu_required=1,
            memory_gb_required=4,
            interruption_probability_threshold=15),
        Deployment.git_repo(
            "https://github.com/kurtschelfthout/meadowrun-test",
            conda_yml_file="../env.yml",
            branch="master",
            commit="master",
            path_in_repo="src"
        )
    )
    print(f"It worked, got {result=}")

if __name__ == "__main__":
    asyncio.run(main())
    
