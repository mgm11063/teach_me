import type { Metadata } from 'next'
import QuestionCards from "@/components/QuestionCards";
import { getServerSideData } from "@/libs/service/getServerSideData";

export const metadata: Metadata = {
    title: 'Questions',
    description: 'Questions',
}
export const getServerSideProps = getServerSideData('https://api.example.com/data');

export default function Questions({ error }) {
    const projects = [
        {
            id: 1,
            title: '타이틀 입니다.',
            description: '설명 입니다.',
            percentageComplete: 26,
            date: '3일 남음',
            users: [
                { id: 1, name: '케인', avatar: 'https://static-cdn.jtvnw.net/jtv_user_pictures/66f0c1c8-e9d3-40ba-a626-e359dc4acb51-profile_image-300x300.png' },
            ],
        },
    ];
    if (error) {
        return <div>Error loading data</div>;
    }
    return (
        <>
            <div>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
                    {projects.map(project => (
                        <QuestionCards key={project.id} {...project} />
                    ))}
                </div>
            </div>

        </>
    );
}
