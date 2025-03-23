const AIXPLAIN_API_KEY = "127ac171414ce790d81e4f9da29069f2d249caf226b95af7024aafa9b54a306c";

const AGENT_ID = '67dec93a338999cb9696a1bb';
const POST_URL = `https://platform-api.aixplain.com/sdk/agents/${AGENT_ID}/run`;

const data = {
	"query": "<QUERY_TEXT_DATA>",
	"sessionId": "<SESSIONID_TEXT_DATA>" // Optional: Specify sessionId the from previous message
};

async function runAgent() {
	try {
		const postResponse = await fetch(POST_URL, {
			method: 'POST',
			headers: {
				'x-api-key': AIXPLAIN_API_KEY,
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		});
		const postResult = await postResponse.json();
		const requestId = postResult.requestId;
		const getUrl = `https://platform-api.aixplain.com/sdk/agents/${requestId}/result`;

		while (true) {
			const getResponse = await fetch(getUrl, {
				method: 'GET',
				headers: {
					'x-api-key': AIXPLAIN_API_KEY,
					'Content-Type': 'application/json'
				}
			});
			const result = await getResponse.json();

			if (result.completed) {
				console.log(result);
				break;
			} else {
				await new Promise(resolve => setTimeout(resolve, 5000)); // Wait for 5 seconds before checking the result again
			}
		}
	} catch (error) {
		console.error(error);
	}
}

runAgent();
