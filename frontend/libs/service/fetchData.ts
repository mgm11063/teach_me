async function fetchData(url: string): Promise<any> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch data: ${res.status}`);
  }
  const data = await res.json();
  return data;
}

export default fetchData;
