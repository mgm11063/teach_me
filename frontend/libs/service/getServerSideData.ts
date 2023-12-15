import { GetServerSideProps } from "next";
import fetchData from "./fetchData";

export const getServerSideData = (
  url: string,
  options?: RequestInit
): GetServerSideProps => {
  return async (context) => {
    const data = await fetchData(url, options);
    return { props: { data } };
  };
};
