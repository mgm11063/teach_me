import QuestionCards from "@/components/QuestionCards";

export default function Questions() {


    const projects = [
        {
            id: 1,
            title: '망포역 비상주사무실 계약 질문',
            description: '안녕하세요, 스마트스토어 개설 위해 비상주사무실 알아보고 있는 중입니다. (거주지 개인주소 노출이 싫어서 새로운 주소 원함)망포역 근처에 몇 군데 있던데 혹시 계약하신 분 계실까요? 가격이나 후기 좀 알고 싶습니다^^',
            percentageComplete: 56,
            date: '3 days left',
            users: [
                { id: 1, name: 'Alice', avatar: 'https://static-cdn.jtvnw.net/jtv_user_pictures/66f0c1c8-e9d3-40ba-a626-e359dc4acb51-profile_image-300x300.png' },
            ],
        },
    ];
    return (
        <>
            <div className="p-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
                    {projects.map(project => (
                        <QuestionCards key={project.id} {...project} />
                    ))}
                </div>
            </div>

        </>
    );
}
