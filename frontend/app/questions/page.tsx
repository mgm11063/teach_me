import type { Metadata } from 'next'
import QuestionCards from "@/components/QuestionCards";

export const metadata: Metadata = {
    title: 'Questions',
    description: 'Questions',
}


export default function Questions() {
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
