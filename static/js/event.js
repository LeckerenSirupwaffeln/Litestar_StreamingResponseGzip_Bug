function StartRetrievingData()
{    
  keep_running = true;
  RetrieveNewData();
}

function StopRetrievingData()
{
  keep_running = false;
}

async function RetrieveNewData() 
{
  const response = await fetch('', {
    method: "POST",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  });

  const reader = response.body.getReader();
  
  while (true) 
  {
    const { done, value } = await reader.read();
    if (value)
    {
      const decoded_data = new TextDecoder().decode(value);
      console.log(decoded_data);
    }

    if (done || !keep_running) 
    {
      console.log("done or not keep_running");
      return;
    }
  }
}