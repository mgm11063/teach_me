const QuestionCards = ({ id, title, content, reward, categories, users }) => {
    return (
        <div className="group border p-4 rounded-lg shadow-lg bg-C-dark-200 hover:bg-black hover:text-white transition duration-300 ease-in-out">
            <h3 className="text-lg font-bold">{title}</h3>
            <p className="text-sm mt-5 group-hover:text-gray-300 transition duration-300 ease-in-out line-clamp-2" >{content}</p>
            <div className="my-5">
                <div className="my-2 flex justify-between items-center">
                    <div className="w-full  rounded-full h-2.5 mr-2">
                        <div
                            className="bg-blue-600 h-2.5 rounded-full"
                            style={{ width: `55%` }}
                        ></div>
                    </div>
                    <span className="text-sm font-bold">{55}%</span>
                </div>
            </div>
            <div className="flex justify-between items-center text-xs">
                <span>10일전</span>
                <div>
                    {users.map(user => (
                        <img key={user.id} src={user.avatar} alt={user.name} className="inline-block h-6 w-6 rounded-full" />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default QuestionCards;