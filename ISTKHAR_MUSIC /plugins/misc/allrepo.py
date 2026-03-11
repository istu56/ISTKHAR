from pyrogram import filters
from ISTKHAR_MUSIC import app
import aiohttp

def chunk_string(text, size=4000):
    return [text[i:i + size] for i in range(0, len(text), size)]

@app.on_message(filters.command("allrepo"))
async def all_repo_command(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ 𝐔𝐬𝐚𝐠𝐞:\n`/allrepo github_username`\n\n𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n`/allrepo torvalds`"
        )

    username = message.command[1]
    api_url = f"https://api.github.com/users/{username}/repos?per_page=100"

    loading = await message.reply_text("🚀 𝐅𝐞𝐭𝐜𝐡𝐢𝐧𝐠 𝐑𝐞𝐩𝐨𝐬𝐢𝐭𝐨𝐫𝐢𝐞𝐬...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:

                if response.status == 404:
                    return await loading.edit("❌ 𝐆𝐢𝐭𝐇𝐮𝐛 𝐔𝐬𝐞𝐫 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝")

                if response.status == 403:
                    return await loading.edit("⚠️ 𝐆𝐢𝐭𝐇𝐮𝐛 𝐑𝐚𝐭𝐞 𝐋𝐢𝐦𝐢𝐭 𝐄𝐱𝐜𝐞𝐞𝐝𝐞𝐝")

                if response.status != 200:
                    return await loading.edit("⚠️ 𝐆𝐢𝐭𝐇𝐮𝐛 𝐀𝐏𝐈 𝐄𝐫𝐫𝐨𝐫")

                repos = await response.json()

        if not repos:
            return await loading.edit("📂 𝐍𝐨 𝐑𝐞𝐩𝐨𝐬𝐢𝐭𝐨𝐫𝐢𝐞𝐬 𝐅𝐨𝐮𝐧𝐝")

        repos = sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)

        total_repos = len(repos)
        total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)

        header = (
            f"╔═══❖•ೋ° 𝐆𝐈𝐓𝐇𝐔𝐁 𝐑𝐄𝐏𝐎 𝐋𝐈𝐒𝐓 °ೋ•❖═══╗\n"
            f"👤 𝐔𝐬𝐞𝐫 : {username}\n"
            f"📦 𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐩𝐨𝐬 : {total_repos}\n"
            f"⭐ 𝐓𝐨𝐭𝐚𝐥 𝐒𝐭𝐚𝐫𝐬 : {total_stars}\n"
            f"╚════════════════════════════╝\n\n"
        )

        repo_text = ""

        for repo in repos:
            repo_text += (
                f"➤ 𝐑𝐞𝐩𝐨 : {repo.get('name')}\n"
                f"   ⭐ 𝐒𝐭𝐚𝐫𝐬 : {repo.get('stargazers_count', 0)}  |  "
                f"🍴 𝐅𝐨𝐫𝐤𝐬 : {repo.get('forks_count', 0)}\n"
                f"   📝 {repo.get('description') or '𝐍𝐨 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧'}\n"
                f"   🔗 {repo.get('html_url')}\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
            )

        final_text = header + repo_text
        chunks = chunk_string(final_text)

        await loading.delete()

        for chunk in chunks:
            await message.reply_text(
                chunk,
                disable_web_page_preview=True
            )

    except Exception as e:
        await loading.edit(f"⚠️ 𝐄𝐫𝐫𝐨𝐫 : {str(e)}")
