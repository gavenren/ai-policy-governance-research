# Repository establishment

State: setup verification record; no completed paper.

- Repository: https://github.com/gavenren/ai-policy-governance-research
- GitHub repository ID: `1412560822`.
- Owner verified through the connected GitHub account: `gavenren`.
- Name availability verified in GitHub's new-repository form before creation.
- Created: `2026-10-09T23:42:29Z` according to the public repository API.
- Visibility: `public`; public API returned `private: false` and `visibility: public`.
- Reuse licence: none selected; public API returned `license: null`.
- Initial commit: [`61850654f5bc96f278c98b57b56b30ec574d8796`](https://github.com/gavenren/ai-policy-governance-research/commit/61850654f5bc96f278c98b57b56b30ec574d8796).
- Initial commit time: `2026-10-09T23:43:32Z`.
- Commit content inspected using the GitHub commit API; it contains the initial README and labels the programme as setup.
- Verification: local `git log -1 --format=%H` and public `git ls-remote origin refs/heads/main` both returned that exact SHA after fetching the initial commit.

Creation and initial commit used an already authenticated GitHub browser session. No credentials were created and no account settings were changed. The repository is separate from `gavenren/ai-safety-research`, which was only read for duplicate avoidance.

## Available publication access

The connector can read the new repository but its first file-write attempt returned `403 Resource not accessible by integration`. Existing HTTPS Git authentication was unavailable; a no-prompt dry run could not obtain a username. SSH strict host verification had no existing trusted host entry. No credential, trust, or permission configuration was changed. The already authenticated browser successfully published the initial commit and remains the publication path.
