interface Media {
  file: string;
}

interface Category {
  id: number;
  name: string;
  description?: string;
}

interface Answer {
  id: number;
  created_at: string;
  updated_at: string;
  content: string;
  is_accepted: boolean;
  user: number;
  question: number;
}

interface Question {
  media: Media[];
  title: string;
  content: string;
  reward: number;
  user: User;
  categories: Category[];
  answers: Answer[];
}

interface Questions {
  id: number;
  title: string;
  content: string;
  reward: number;
  user: User;
  categories: Category[];
}

type QuestionsArray = Questions[];

interface User {
  id: number;
  username: string;
  phone_number: string;
  email: string;
  first_name: string;
  last_name: string;
  answers: Answer[];
  questions: Question[];
}
