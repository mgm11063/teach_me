// libs/fetchData.ts
async function fetchData(url: string, options: RequestInit = {}): Promise<any> {
  const res = await fetch(url, options);
  if (!res.ok) {
    throw new Error(`Failed to fetch data: ${res.status}`);
  }
  const data = await res.json();
  return data;
}

export default fetchData;
